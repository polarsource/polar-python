"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from typing import (
    Any,
    Dict,
    get_type_hints,
    List,
    Tuple,
)
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from .serializers import marshal_json

from .metadata import (
    FormMetadata,
    MultipartFormMetadata,
    find_field_metadata,
)
from .values import _is_set, _val_to_string


def _populate_form(
    field_name: str,
    explode: bool,
    obj: Any,
    delimiter: str,
    form: Dict[str, List[str]],
):
    if not _is_set(obj):
        return form

    if isinstance(obj, BaseModel):
        items = []

        obj_fields: Dict[str, FieldInfo] = obj.__class__.model_fields
        for name in obj_fields:
            obj_field = obj_fields[name]
            obj_field_name = obj_field.alias if obj_field.alias is not None else name
            if obj_field_name == "":
                continue

            val = getattr(obj, name)
            if not _is_set(val):
                continue

            if explode:
                form[obj_field_name] = [_val_to_string(val)]
            else:
                items.append(f"{obj_field_name}{delimiter}{_val_to_string(val)}")

        if len(items) > 0:
            form[field_name] = [delimiter.join(items)]
    elif isinstance(obj, Dict):
        items = []
        for key, value in obj.items():
            if not _is_set(value):
                continue

            if explode:
                form[key] = [_val_to_string(value)]
            else:
                items.append(f"{key}{delimiter}{_val_to_string(value)}")

        if len(items) > 0:
            form[field_name] = [delimiter.join(items)]
    elif isinstance(obj, List):
        items = []

        for value in obj:
            if not _is_set(value):
                continue

            if explode:
                if not field_name in form:
                    form[field_name] = []
                form[field_name].append(_val_to_string(value))
            else:
                items.append(_val_to_string(value))

        if len(items) > 0:
            form[field_name] = [delimiter.join([str(item) for item in items])]
    else:
        form[field_name] = [_val_to_string(obj)]

    return form


def _extract_file_properties(file_obj: Any) -> Tuple[str, Any, Any]:
    """Extract file name, content, and content type from a file object."""
    file_fields: Dict[str, FieldInfo] = file_obj.__class__.model_fields

    file_name = ""
    content = None
    content_type = None

    for file_field_name in file_fields:
        file_field = file_fields[file_field_name]

        file_metadata = find_field_metadata(file_field, MultipartFormMetadata)
        if file_metadata is None:
            continue

        if file_metadata.content:
            content = getattr(file_obj, file_field_name, None)
        elif file_field_name == "content_type":
            content_type = getattr(file_obj, file_field_name, None)
        else:
            file_name = getattr(file_obj, file_field_name)

    if file_name == "" or content is None:
        raise ValueError("invalid multipart/form-data file")

    return file_name, content, content_type


def serialize_multipart_form(
    media_type: str, request: Any
) -> Tuple[str, Dict[str, Any], List[Tuple[str, Any]]]:
    form: Dict[str, Any] = {}
    files: List[Tuple[str, Any]] = []

    if not isinstance(request, BaseModel):
        raise TypeError("invalid request body type")

    request_fields: Dict[str, FieldInfo] = request.__class__.model_fields
    request_field_types = get_type_hints(request.__class__)

    for name in request_fields:
        field = request_fields[name]

        val = getattr(request, name)
        if not _is_set(val):
            continue

        field_metadata = find_field_metadata(field, MultipartFormMetadata)
        if not field_metadata:
            continue

        f_name = field.alias if field.alias else name

        if field_metadata.file:
            if isinstance(val, List):
                # Handle array of files
                for file_obj in val:
                    if not _is_set(file_obj):
                        continue
                        
                    file_name, content, content_type = _extract_file_properties(file_obj)

                    if content_type is not None:
                        files.append((f_name + "[]", (file_name, content, content_type)))
                    else:
                        files.append((f_name + "[]", (file_name, content)))
            else:
                # Handle single file
                file_name, content, content_type = _extract_file_properties(val)

                if content_type is not None:
                    files.append((f_name, (file_name, content, content_type)))
                else:
                    files.append((f_name, (file_name, content)))
        elif field_metadata.json:
            files.append((f_name, (
                None,
                marshal_json(val, request_field_types[name]),
                "application/json",
            )))
        else:
            if isinstance(val, List):
                values = []

                for value in val:
                    if not _is_set(value):
                        continue
                    values.append(_val_to_string(value))

                form[f_name + "[]"] = values
            else:
                form[f_name] = _val_to_string(val)
    return media_type, form, files


def serialize_form_data(data: Any) -> Dict[str, Any]:
    form: Dict[str, List[str]] = {}

    if isinstance(data, BaseModel):
        data_fields: Dict[str, FieldInfo] = data.__class__.model_fields
        data_field_types = get_type_hints(data.__class__)
        for name in data_fields:
            field = data_fields[name]

            val = getattr(data, name)
            if not _is_set(val):
                continue

            metadata = find_field_metadata(field, FormMetadata)
            if metadata is None:
                continue

            f_name = field.alias if field.alias is not None else name

            if metadata.json:
                form[f_name] = [marshal_json(val, data_field_types[name])]
            else:
                if metadata.style == "form":
                    _populate_form(
                        f_name,
                        metadata.explode,
                        val,
                        ",",
                        form,
                    )
                else:
                    raise ValueError(f"Invalid form style for field {name}")
    elif isinstance(data, Dict):
        for key, value in data.items():
            if _is_set(value):
                form[key] = [_val_to_string(value)]
    else:
        raise TypeError(f"Invalid request body type {type(data)} for form data")

    return form
