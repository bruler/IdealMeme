# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/features/template_features_req.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/features/template_features_req.proto',
  package='template_feature_requirements',
  syntax='proto3',
  serialized_pb=_b('\n(src/features/template_features_req.proto\x12\x1dtemplate_feature_requirements\"\x0b\n\tM_Helmets\"\r\n\x0bM_Helmets_F\"\x08\n\x06Online\"\x10\n\x0eNxt_Thrty_Days\"\x11\n\x0fLng_Time_No_See\"\xd4\x02\n\rTemplates_Req\x12;\n\tm_helmets\x18\x01 \x01(\x0b\x32(.template_feature_requirements.M_Helmets\x12?\n\x0bm_helmets_f\x18\x02 \x01(\x0b\x32*.template_feature_requirements.M_Helmets_F\x12\x35\n\x06online\x18\x03 \x01(\x0b\x32%.template_feature_requirements.Online\x12\x45\n\x0enxt_thrty_days\x18\x04 \x01(\x0b\x32-.template_feature_requirements.Nxt_Thrty_Days\x12G\n\x0flng_time_no_see\x18\x05 \x01(\x0b\x32..template_feature_requirements.Lng_Time_No_See\"L\n\tTemplates\x12?\n\ttemplates\x18\x01 \x03(\x0b\x32,.template_feature_requirements.Templates_Reqb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_M_HELMETS = _descriptor.Descriptor(
  name='M_Helmets',
  full_name='template_feature_requirements.M_Helmets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=86,
)


_M_HELMETS_F = _descriptor.Descriptor(
  name='M_Helmets_F',
  full_name='template_feature_requirements.M_Helmets_F',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=101,
)


_ONLINE = _descriptor.Descriptor(
  name='Online',
  full_name='template_feature_requirements.Online',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=111,
)


_NXT_THRTY_DAYS = _descriptor.Descriptor(
  name='Nxt_Thrty_Days',
  full_name='template_feature_requirements.Nxt_Thrty_Days',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=129,
)


_LNG_TIME_NO_SEE = _descriptor.Descriptor(
  name='Lng_Time_No_See',
  full_name='template_feature_requirements.Lng_Time_No_See',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=148,
)


_TEMPLATES_REQ = _descriptor.Descriptor(
  name='Templates_Req',
  full_name='template_feature_requirements.Templates_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m_helmets', full_name='template_feature_requirements.Templates_Req.m_helmets', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m_helmets_f', full_name='template_feature_requirements.Templates_Req.m_helmets_f', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online', full_name='template_feature_requirements.Templates_Req.online', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nxt_thrty_days', full_name='template_feature_requirements.Templates_Req.nxt_thrty_days', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lng_time_no_see', full_name='template_feature_requirements.Templates_Req.lng_time_no_see', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=491,
)


_TEMPLATES = _descriptor.Descriptor(
  name='Templates',
  full_name='template_feature_requirements.Templates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='templates', full_name='template_feature_requirements.Templates.templates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=569,
)

_TEMPLATES_REQ.fields_by_name['m_helmets'].message_type = _M_HELMETS
_TEMPLATES_REQ.fields_by_name['m_helmets_f'].message_type = _M_HELMETS_F
_TEMPLATES_REQ.fields_by_name['online'].message_type = _ONLINE
_TEMPLATES_REQ.fields_by_name['nxt_thrty_days'].message_type = _NXT_THRTY_DAYS
_TEMPLATES_REQ.fields_by_name['lng_time_no_see'].message_type = _LNG_TIME_NO_SEE
_TEMPLATES.fields_by_name['templates'].message_type = _TEMPLATES_REQ
DESCRIPTOR.message_types_by_name['M_Helmets'] = _M_HELMETS
DESCRIPTOR.message_types_by_name['M_Helmets_F'] = _M_HELMETS_F
DESCRIPTOR.message_types_by_name['Online'] = _ONLINE
DESCRIPTOR.message_types_by_name['Nxt_Thrty_Days'] = _NXT_THRTY_DAYS
DESCRIPTOR.message_types_by_name['Lng_Time_No_See'] = _LNG_TIME_NO_SEE
DESCRIPTOR.message_types_by_name['Templates_Req'] = _TEMPLATES_REQ
DESCRIPTOR.message_types_by_name['Templates'] = _TEMPLATES

M_Helmets = _reflection.GeneratedProtocolMessageType('M_Helmets', (_message.Message,), dict(
  DESCRIPTOR = _M_HELMETS,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.M_Helmets)
  ))
_sym_db.RegisterMessage(M_Helmets)

M_Helmets_F = _reflection.GeneratedProtocolMessageType('M_Helmets_F', (_message.Message,), dict(
  DESCRIPTOR = _M_HELMETS_F,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.M_Helmets_F)
  ))
_sym_db.RegisterMessage(M_Helmets_F)

Online = _reflection.GeneratedProtocolMessageType('Online', (_message.Message,), dict(
  DESCRIPTOR = _ONLINE,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.Online)
  ))
_sym_db.RegisterMessage(Online)

Nxt_Thrty_Days = _reflection.GeneratedProtocolMessageType('Nxt_Thrty_Days', (_message.Message,), dict(
  DESCRIPTOR = _NXT_THRTY_DAYS,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.Nxt_Thrty_Days)
  ))
_sym_db.RegisterMessage(Nxt_Thrty_Days)

Lng_Time_No_See = _reflection.GeneratedProtocolMessageType('Lng_Time_No_See', (_message.Message,), dict(
  DESCRIPTOR = _LNG_TIME_NO_SEE,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.Lng_Time_No_See)
  ))
_sym_db.RegisterMessage(Lng_Time_No_See)

Templates_Req = _reflection.GeneratedProtocolMessageType('Templates_Req', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATES_REQ,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.Templates_Req)
  ))
_sym_db.RegisterMessage(Templates_Req)

Templates = _reflection.GeneratedProtocolMessageType('Templates', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATES,
  __module__ = 'src.features.template_features_req_pb2'
  # @@protoc_insertion_point(class_scope:template_feature_requirements.Templates)
  ))
_sym_db.RegisterMessage(Templates)


# @@protoc_insertion_point(module_scope)