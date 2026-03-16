def generate_email_list(candidate_df):

    emails = candidate_df["Email"].dropna().tolist()

    email_string = "; ".join(emails)

    return email_string