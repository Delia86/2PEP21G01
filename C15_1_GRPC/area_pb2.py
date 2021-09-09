# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: area.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='area.proto',
  package='C15_1_GRPC',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\narea.proto\x12\nC15_1_GRPC\"+\n\nAreaParams\x12\x0e\n\x06lenght\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\"\x1c\n\nAreaResult\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32S\n\x0e\x41reaCalculator\x12\x41\n\rCalculateArea\x12\x16.C15_1_GRPC.AreaParams\x1a\x16.C15_1_GRPC.AreaResult\"\x00\x62\x06proto3'
)




_AREAPARAMS = _descriptor.Descriptor(
  name='AreaParams',
  full_name='C15_1_GRPC.AreaParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lenght', full_name='C15_1_GRPC.AreaParams.lenght', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='C15_1_GRPC.AreaParams.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=69,
)


_AREARESULT = _descriptor.Descriptor(
  name='AreaResult',
  full_name='C15_1_GRPC.AreaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='C15_1_GRPC.AreaResult.result', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['AreaParams'] = _AREAPARAMS
DESCRIPTOR.message_types_by_name['AreaResult'] = _AREARESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AreaParams = _reflection.GeneratedProtocolMessageType('AreaParams', (_message.Message,), {
  'DESCRIPTOR' : _AREAPARAMS,
  '__module__' : 'area_pb2'
  # @@protoc_insertion_point(class_scope:C15_1_GRPC.AreaParams)
  })
_sym_db.RegisterMessage(AreaParams)

AreaResult = _reflection.GeneratedProtocolMessageType('AreaResult', (_message.Message,), {
  'DESCRIPTOR' : _AREARESULT,
  '__module__' : 'area_pb2'
  # @@protoc_insertion_point(class_scope:C15_1_GRPC.AreaResult)
  })
_sym_db.RegisterMessage(AreaResult)



_AREACALCULATOR = _descriptor.ServiceDescriptor(
  name='AreaCalculator',
  full_name='C15_1_GRPC.AreaCalculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=101,
  serialized_end=184,
  methods=[
  _descriptor.MethodDescriptor(
    name='CalculateArea',
    full_name='C15_1_GRPC.AreaCalculator.CalculateArea',
    index=0,
    containing_service=None,
    input_type=_AREAPARAMS,
    output_type=_AREARESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AREACALCULATOR)

DESCRIPTOR.services_by_name['AreaCalculator'] = _AREACALCULATOR

# @@protoc_insertion_point(module_scope)