# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profanedb/protobuf/options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='profanedb/protobuf/options.proto',
  package='profanedb.protobuf',
  syntax='proto2',
  serialized_pb=_b('\n profanedb/protobuf/options.proto\x12\x12profanedb.protobuf\x1a google/protobuf/descriptor.proto\"\x1b\n\x0c\x46ieldOptions\x12\x0b\n\x03key\x18\x01 \x01(\x08:Q\n\x07options\x12\x1d.google.protobuf.FieldOptions\x18\x8c\x08 \x01(\x0b\x32 .profanedb.protobuf.FieldOptionsBZ\n\x16\x63om.profanedb.protobufZ%gitlab.com/profanedb/protobuf/options\xa2\x02\x03PDB\xaa\x02\x12ProfaneDB.Protobuf')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


OPTIONS_FIELD_NUMBER = 1036
options = _descriptor.FieldDescriptor(
  name='options', full_name='profanedb.protobuf.options', index=0,
  number=1036, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_FIELDOPTIONS = _descriptor.Descriptor(
  name='FieldOptions',
  full_name='profanedb.protobuf.FieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='profanedb.protobuf.FieldOptions.key', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['FieldOptions'] = _FIELDOPTIONS
DESCRIPTOR.extensions_by_name['options'] = options

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _FIELDOPTIONS,
  __module__ = 'profanedb.protobuf.options_pb2'
  # @@protoc_insertion_point(class_scope:profanedb.protobuf.FieldOptions)
  ))
_sym_db.RegisterMessage(FieldOptions)

options.message_type = _FIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(options)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.profanedb.protobufZ%gitlab.com/profanedb/protobuf/options\242\002\003PDB\252\002\022ProfaneDB.Protobuf'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
