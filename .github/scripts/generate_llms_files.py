import argparse
import os
import toml
from pathlib import Path
from urllib.parse import urljoin
import re
from typing import List, Optional, Tuple


def _construct_url(base_url: Optional[str], relative_path: str) -> str:
    """Constructs an absolute URL if base_url is provided, otherwise returns relative_path."""
    if not base_url:
        # If no base URL, return the relative path as is (or adjust if needed based on output location)
        # Assuming output is at repo root, the relative path from repo root is correct.
        return relative_path 

    # Ensure base_url ends with a slash for urljoin
    temp_base_url = base_url
    if not temp_base_url.endswith('/'):
        temp_base_url += '/'

    # urljoin handles joining base and relative path correctly
    # It correctly handles paths starting with '/' or not.
    return urljoin(temp_base_url, relative_path)

def find_md_files(directory: Path) -> List[Path]:
    """Recursively finds all Markdown files in a directory."""
    return list(Path(directory).rglob('*.md'))

def get_project_metadata(repo_root: Path) -> Tuple[str, str]:
    """Reads project metadata from pyproject.toml."""
    pyproject_path = Path(repo_root) / 'pyproject.toml'
    if not pyproject_path.exists():
        print(f"Warning: pyproject.toml not found at {pyproject_path}")
        return "Unknown Project", "No description found."
    
    try:
        data = toml.load(pyproject_path)
        name = data.get('tool', {}).get('poetry', {}).get('name', 'Polar')
        description = data.get('tool', {}).get('poetry', {}).get('description', 'Polar SDK Python')
        return name, description
    except Exception as e:
        print(f"Error reading pyproject.toml: {e}")
        return "Unknown Project", "Error reading description."

def generate_llms_txt(project_name: str, description: str, md_files: List[Path], repo_root: Path, docs_dir_path: Path, base_url: Optional[str] = None) -> str:
    """Generates the llms.txt file content."""
    content = f"# {project_name}\n\n"
    content += f"> {description}\n\n"
    
    # Create dynamic header from the scanned directory name
    dir_name = docs_dir_path.name.replace('_', ' ').replace('-', ' ').title()
    content += f"## {dir_name} Files\n\n"
    
    if not md_files:
        content += "- No Markdown documentation files found.\n"
    else:
        for md_path in sorted(md_files):
            # Relative path from repo root is needed for URL construction or relative link
            relative_path = md_path.relative_to(repo_root).as_posix()
            # Use the capitalized parent directory name as the link title
            link_title = md_path.parent.name.capitalize()

            # Use the helper function to construct the URL
            link_url = _construct_url(base_url, relative_path)

            content += f"- [{link_title}]({link_url})\n"
            
    content += "\n## Optional\n"
    # Construct the link for llms-full.txt using the helper function
    extended_context_link = _construct_url(base_url, "llms-full.txt")
        
    content += f"- [Extended Context]({extended_context_link})\n"
    
    return content

def generate_llms_full_txt(llms_txt_content: str, md_files: List[Path], repo_root: Path, base_url: Optional[str] = None) -> str:
    """Generates the llms-full.txt file content, adjusting heading levels and adding raw links."""
    full_content = llms_txt_content
    full_content += "\n\n---\n\n# Full Content Details\n\n"
    
    if not md_files:
        full_content += "No Markdown documentation files found to include.\n"
    else:
        for md_path in sorted(md_files):
            relative_path = md_path.relative_to(repo_root)
            relative_path_posix = relative_path.as_posix()
            
            # Construct the link URL using the helper function
            link_url = _construct_url(base_url, relative_path_posix)
            
            # Determine the header link based on whether a URL was constructed
            header_link = f"[{relative_path_posix}]({link_url})" if base_url else relative_path_posix

            try:
                file_content = md_path.read_text(encoding='utf-8')
                # Adjust heading levels: Add two '#' to each heading line (H1->H3, H2->H4, etc.)
                adjusted_content = re.sub(r'^(#+ )', r'##\1', file_content, flags=re.MULTILINE)
                
                full_content += f"## Content: {header_link}\n\n"
                full_content += adjusted_content
                full_content += "\n\n---\n\n"
            except Exception as e:
                full_content += f"## Content: {header_link}\n\n" # Still add link even if read fails
                full_content += f"Error reading file: {e}\n\n---\n\n"
                
    return full_content

def main() -> None:
    parser = argparse.ArgumentParser(description='Generate llms.txt and llms-full.txt for a project.')
    parser.add_argument('--dir', required=True, help='Directory to scan for Markdown files (e.g., docs).')
    parser.add_argument('--output', default='.', help='Output directory for llms.txt and llms-full.txt.')
    parser.add_argument('--repo-root', default='.', help='Path to the repository root.')
    parser.add_argument('--base-url', default=None, help='Optional base URL for constructing absolute links (e.g., GitHub raw URL).')
    
    args = parser.parse_args()

    docs_dir_path = Path(args.repo_root) / args.dir
    output_dir_path = Path(args.output)
    repo_root_path = Path(args.repo_root)

    if not docs_dir_path.is_dir():
        print(f"Error: Documentation directory not found: {docs_dir_path}")
        return

    output_dir_path.mkdir(parents=True, exist_ok=True)

    project_name, description = get_project_metadata(repo_root_path)
    md_files = find_md_files(docs_dir_path)
    
    # Ensure paths in md_files are relative to repo_root for consistency
    md_files_relative_to_root = [f.relative_to(repo_root_path) for f in md_files]
    # Get absolute paths again for reading/linking
    md_files_abs = [repo_root_path / f for f in md_files_relative_to_root]

    # --- Generate llms.txt ---
    print(f"Generating llms.txt in {output_dir_path}...")
    llms_txt_content = generate_llms_txt(project_name, description, md_files_abs, repo_root_path, docs_dir_path, args.base_url)
    llms_txt_file = output_dir_path / 'llms.txt'
    try:
        llms_txt_file.write_text(llms_txt_content, encoding='utf-8')
        print(f"Successfully wrote {llms_txt_file}")
    except Exception as e:
        print(f"Error writing {llms_txt_file}: {e}")

    # --- Generate llms-full.txt ---
    print(f"Generating llms-full.txt in {output_dir_path}...")
    # Pass the *generated* content of llms.txt, md_files, repo_root, and base_url
    llms_full_content = generate_llms_full_txt(llms_txt_content, md_files_abs, repo_root_path, args.base_url)
    llms_full_txt_file = output_dir_path / 'llms-full.txt'
    try:
        llms_full_txt_file.write_text(llms_full_content, encoding='utf-8')
        print(f"Successfully wrote {llms_full_txt_file}")
    except Exception as e:
        print(f"Error writing {llms_full_txt_file}: {e}")

if __name__ == "__main__":
    main()
