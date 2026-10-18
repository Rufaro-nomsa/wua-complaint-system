# Women's University Complaint Reporting System
# Week 8: Unit Testing

def validate_complaint(description):
    """
    Check whether a complaint description is valid.
    """

    # Reject an empty complaint
    if not description:
        return False

    # Reject a complaint containing only spaces
    if description.strip() == "":
        return False

    # Accept a complaint with a description
    return True