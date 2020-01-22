######################################################################
# Input filename: /Users/hodapp/Development/HiveWeb/dbicdh/_source/deploy/15/001-auto.yml
# Generated on Tue Jan 21 19:07:20 2020 by ./catalyst_to_sqlalchemy.py
# Begin automatically generated code:
######################################################################
import sqlalchemy
import sqlalchemy.dialects.postgresql
import citext

access_log = sqlalchemy.Table('access_log', metadata,
    sqlalchemy.Column('access_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('access_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('badge_id', sqlalchemy.Integer),
    sqlalchemy.Column('granted', sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column('item_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID),
)

action = sqlalchemy.Table('action', metadata,
    sqlalchemy.Column('action_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('action_type', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('priority', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('queued_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('queuing_member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('row_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

application = sqlalchemy.Table('application', metadata,
    sqlalchemy.Column('address1', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('address2', sqlalchemy.VARCHAR),
    sqlalchemy.Column('app_turned_in_at', sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column('application_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('city', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('contact_name', sqlalchemy.VARCHAR),
    sqlalchemy.Column('contact_phone', sqlalchemy.BigInteger),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('decided_at', sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column('final_result', sqlalchemy.VARCHAR),
    sqlalchemy.Column('form_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('helper', sqlalchemy.VARCHAR),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('picture_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('state', sqlalchemy.CHAR, nullable=False),
    sqlalchemy.Column('thread_message_id', sqlalchemy.VARCHAR),
    sqlalchemy.Column('topic_id', sqlalchemy.VARCHAR),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('zip', sqlalchemy.CHAR, nullable=False),
)

audit_log = sqlalchemy.Table('audit_log', metadata,
    sqlalchemy.Column('audit_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('change_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('change_type', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('changed_member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('changing_member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('notes', sqlalchemy.VARCHAR),
)

badge = sqlalchemy.Table('badge', metadata,
    sqlalchemy.Column('badge_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('badge_number', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

curse = sqlalchemy.Table('curse', metadata,
    sqlalchemy.Column('curse_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('display_name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('notification_markdown', sqlalchemy.Text),
    sqlalchemy.Column('priority', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('protect_group_cast', sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column('protect_user_cast', sqlalchemy.Boolean, nullable=False),
)

curse_action = sqlalchemy.Table('curse_action', metadata,
    sqlalchemy.Column('action', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('curse_action_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('curse_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('message', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('path', sqlalchemy.VARCHAR, nullable=False),
)

device = sqlalchemy.Table('device', metadata,
    sqlalchemy.Column('device_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('key', sqlalchemy.dialects.postgresql.BYTEA, nullable=False),
    sqlalchemy.Column('max_version', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('min_version', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('nonce', sqlalchemy.dialects.postgresql.BYTEA),
)

device_item = sqlalchemy.Table('device_item', metadata,
    sqlalchemy.Column('device_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('item_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

image = sqlalchemy.Table('image', metadata,
    sqlalchemy.Column('content_type', sqlalchemy.VARCHAR),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('image', sqlalchemy.dialects.postgresql.BYTEA, nullable=False),
    sqlalchemy.Column('image_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('thumbnail', sqlalchemy.dialects.postgresql.BYTEA),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime(timezone=True), nullable=False),
)

ipn_message = sqlalchemy.Table('ipn_message', metadata,
    sqlalchemy.Column('ipn_message_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('payer_email', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('raw', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('received_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('txn_id', sqlalchemy.VARCHAR),
)

item = sqlalchemy.Table('item', metadata,
    sqlalchemy.Column('display_name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('item_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.CHAR, nullable=False),
    sqlalchemy.Column('scale', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('unit', sqlalchemy.VARCHAR, nullable=False),
)

item_mgroup = sqlalchemy.Table('item_mgroup', metadata,
    sqlalchemy.Column('item_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('mgroup_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

lamp_bulb = sqlalchemy.Table('lamp_bulb', metadata,
    sqlalchemy.Column('bulb_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('color_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('device_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('slot', sqlalchemy.Integer, nullable=False),
)

lamp_bulb_preset = sqlalchemy.Table('lamp_bulb_preset', metadata,
    sqlalchemy.Column('bulb_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('preset_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('value', sqlalchemy.Boolean, nullable=False),
)

lamp_color = sqlalchemy.Table('lamp_color', metadata,
    sqlalchemy.Column('color_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('html_color', sqlalchemy.CHAR, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
)

lamp_preset = sqlalchemy.Table('lamp_preset', metadata,
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('preset_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

log = sqlalchemy.Table('log', metadata,
    sqlalchemy.Column('create_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('log_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('message', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('type', sqlalchemy.VARCHAR, nullable=False),
)

member_curse = sqlalchemy.Table('member_curse', metadata,
    sqlalchemy.Column('curse_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('issued_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('issuing_member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('issuing_notes', sqlalchemy.Text),
    sqlalchemy.Column('lifted_at', sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column('lifting_member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('lifting_notes', sqlalchemy.Text),
    sqlalchemy.Column('member_curse_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

member_mgroup = sqlalchemy.Table('member_mgroup', metadata,
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('mgroup_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

member_panel = sqlalchemy.Table('member_panel', metadata,
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('panel_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer),
    sqlalchemy.Column('style', sqlalchemy.VARCHAR),
    sqlalchemy.Column('visible', sqlalchemy.Boolean),
)

members = sqlalchemy.Table('members', metadata,
    sqlalchemy.Column('alert_credits', sqlalchemy.Integer),
    sqlalchemy.Column('alert_email', sqlalchemy.Boolean),
    sqlalchemy.Column('alert_machine', sqlalchemy.Boolean),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('door_count', sqlalchemy.Integer),
    sqlalchemy.Column('email', citext.CIText, nullable=False, unique=True),
    sqlalchemy.Column('encrypted_password', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('fname', sqlalchemy.VARCHAR),
    sqlalchemy.Column('handle', citext.CIText, unique=True),
    sqlalchemy.Column('linked_member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('lname', sqlalchemy.VARCHAR),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('member_image_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('paypal_email', citext.CIText),
    sqlalchemy.Column('phone', sqlalchemy.BigInteger),
    sqlalchemy.Column('totp_secret', sqlalchemy.dialects.postgresql.BYTEA),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('vend_credits', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('vend_total', sqlalchemy.Integer, nullable=False),
)

mgroup = sqlalchemy.Table('mgroup', metadata,
    sqlalchemy.Column('mgroup_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.CHAR),
)

panel = sqlalchemy.Table('panel', metadata,
    sqlalchemy.Column('large', sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('panel_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('permissions', sqlalchemy.VARCHAR),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('style', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('title', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('visible', sqlalchemy.Boolean, nullable=False),
)

payment = sqlalchemy.Table('payment', metadata,
    sqlalchemy.Column('ipn_message_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('payment_date', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('payment_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

purchase = sqlalchemy.Table('purchase', metadata,
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('purchase_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('purchased_at', sqlalchemy.Date, nullable=False),
)

purchase_soda = sqlalchemy.Table('purchase_soda', metadata,
    sqlalchemy.Column('purchase_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('soda_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('soda_quantity', sqlalchemy.Integer, nullable=False),
)

reset_token = sqlalchemy.Table('reset_token', metadata,
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('token_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('valid', sqlalchemy.Boolean, nullable=False),
)

session = sqlalchemy.Table('session', metadata,
    sqlalchemy.Column('expires', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('id', sqlalchemy.CHAR, primary_key=True, nullable=False),
    sqlalchemy.Column('session_data', sqlalchemy.Text),
)

sign_in_log = sqlalchemy.Table('sign_in_log', metadata,
    sqlalchemy.Column('email', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('remote_ip', sqlalchemy.dialects.postgresql.INET, nullable=False),
    sqlalchemy.Column('sign_in_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('sign_in_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('valid', sqlalchemy.Boolean, nullable=False),
)

soda_status = sqlalchemy.Table('soda_status', metadata,
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('slot_number', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('soda_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('soda_type_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('sold_out', sqlalchemy.Boolean, nullable=False),
)

soda_type = sqlalchemy.Table('soda_type', metadata,
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('soda_type_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

storage_location = sqlalchemy.Table('storage_location', metadata,
    sqlalchemy.Column('location_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('parent_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer, nullable=False),
)

storage_request = sqlalchemy.Table('storage_request', metadata,
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('decided_at', sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column('deciding_member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('decision_notes', sqlalchemy.Text),
    sqlalchemy.Column('hidden', sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('notes', sqlalchemy.Text),
    sqlalchemy.Column('request_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('slot_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('status', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('type_id', sqlalchemy.dialects.postgresql.UUID),
)

storage_slot = sqlalchemy.Table('storage_slot', metadata,
    sqlalchemy.Column('expire_date', sqlalchemy.DateTime(timezone=True)),
    sqlalchemy.Column('location_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('slot_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('type_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

storage_slot_type = sqlalchemy.Table('storage_slot_type', metadata,
    sqlalchemy.Column('can_request', sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column('default_expire_time', sqlalchemy.VARCHAR),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('type_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

survey = sqlalchemy.Table('survey', metadata,
    sqlalchemy.Column('json_data', sqlalchemy.dialects.postgresql.JSONB),
    sqlalchemy.Column('name', sqlalchemy.VARCHAR),
    sqlalchemy.Column('survey_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('title', sqlalchemy.VARCHAR),
)

survey_answer = sqlalchemy.Table('survey_answer', metadata,
    sqlalchemy.Column('answer_text', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('survey_answer_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('survey_question_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('survey_response_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

survey_choice = sqlalchemy.Table('survey_choice', metadata,
    sqlalchemy.Column('choice_name', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('choice_text', sqlalchemy.VARCHAR),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('survey_choice_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('survey_question_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
)

survey_question = sqlalchemy.Table('survey_question', metadata,
    sqlalchemy.Column('question_text', sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column('sort_order', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('survey_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('survey_question_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

survey_response = sqlalchemy.Table('survey_response', metadata,
    sqlalchemy.Column('created_at', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('survey_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('survey_response_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
)

temp_log = sqlalchemy.Table('temp_log', metadata,
    sqlalchemy.Column('create_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('item_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('temp_log_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('temperature', sqlalchemy.Integer, nullable=False),
)

vend_log = sqlalchemy.Table('vend_log', metadata,
    sqlalchemy.Column('badge_id', sqlalchemy.Integer),
    sqlalchemy.Column('device_id', sqlalchemy.dialects.postgresql.UUID, nullable=False),
    sqlalchemy.Column('member_id', sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column('vend_id', sqlalchemy.dialects.postgresql.UUID, primary_key=True, nullable=False),
    sqlalchemy.Column('vend_time', sqlalchemy.DateTime(timezone=True), nullable=False),
    sqlalchemy.Column('vended', sqlalchemy.Boolean, nullable=False),
)

######################################################################
# End automatically generated code
######################################################################
