import re
from typing import Dict
from flask import jsonify, request

from . import app, db, PHONE_NUMBER_PATTERN, EMAIL_PATTERN, DATE_PATTERN


@app.route('/get_form', methods=['POST'])
def get_form():
    """Получение шаблона."""
    data = defining_types(request.args)
    form = db.forms.find_one({val:key for key, val in data.items()})
    if form and data:
        return jsonify({"template_name": form["template_name"]})
    return jsonify(data)


def defining_types(data: Dict[str, str]) -> Dict[str, str]:
    """Определение типов."""
    typing = [
        lambda x: "phone_type" if re.fullmatch(PHONE_NUMBER_PATTERN, x) else None,
        lambda x: "email_type" if re.fullmatch(EMAIL_PATTERN, x) else None,
        lambda x: "date_type" if re.fullmatch(DATE_PATTERN, x) else None,
    ]
    new_dict = {}
    for key, value in data.items():
        [*map(lambda x: new_dict.update({key: x(value)}) if x(value) else '', typing)]
        if key not in new_dict:
            new_dict.update({key: "text_type"})
    return new_dict
