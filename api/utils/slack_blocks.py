hello_message = "Hi there :wave:"

welcome_attachment = [
    {
        "pretext": "I am here to take some *feedback* about your meeting room.",
        "text": "*_How do you feel about your meeting room?_*",
        "callback_id": "os",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
            {
                "name": "bad",
                "text": "Bad",
                "type": "button",
                "style": "danger",
                "value": "bad"
            },
            {
                "name": "notsure",
                "text": "Not Sure",
                "type": "button",
                "value": "notsure"
            },
            {
                "name": "awesome",
                "text": "Awesome",
                "type": "button",
                "style": "primary",
                "value": "awesome"
            }
        ]
    }
]

feedback_form = {
    "title": "Converge Feedback",
    "submit_label": "Submit",
    "callback_id": "two",
    "elements": [
        {
            "label": "Title",
            "type": "text",
            "name": "feedback_title",
            "placeholder": "Enter feedback title",
        },
        {
            "label": "Feedback",
            "type": "textarea",
            "name": "feedback_description",
            "placeholder": "Enter your feedback",
        }
    ]
}

taking_feedback_message = {
    "as_user": "true",
    "text": "Taking your feedback.",
    "response_type": "ephemeral",
    "replace_original": "true"
}

thank_you_message = {
    "as_user": "true",
    "text": "Thank you for your feedback.",
    "response_type": "ephemeral",
    "replace_original": "true"
}

cancellation_message = {
    "text": "Cool! It is also ok.",
    "response_type": "ephemeral",
    "replace_original": "true"
}
