from jira import JIRA

from .exceptions import JiraException

JIRA_BASE_URL = "<JIRA_BASE_URL>"
PERSONAL_ACCESS_TOKEN = "<YOUR-PERSONAL-ACCESS-TOKEN>"
PROJECT_KEY = "<YOUR_PROJECT_KEY>"


# Replace with your Jira instance URL and Personal Access Token (PAT)
def set_issue_data(description, client_id, issue_type, creation_date):
    issue_summary = f"{PROJECT_KEY}, Desc: {description.split()[0]}... by user {client_id}" \
                    f" in {creation_date}"
    issue_data = {
        "project": {"key": PROJECT_KEY},
        "summary": issue_summary,
        "description": description,
        "issuetype": {"name": issue_type},
    }
    return issue_data


class JiraInstance:

    def __init__(self):

        self.host = JIRA_BASE_URL
        self.pat = PERSONAL_ACCESS_TOKEN
        headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
        headers["Authorization"] = f"Bearer {self.pat}"
        jira = JIRA(server=self.host, options={"headers": headers})
        self.jira = jira

    def create_new_issue(self, issue_data):
        try:
            # Create the issue
            new_issue = self.jira.create_issue(fields=issue_data)

            # Print the key of the created issue
            print("Issue created successfully!")
            print("Issue Key:", new_issue.key)
        except Exception as e:
            print("Failed to create issue:", str(e))

    def create_issue_from_backend(self, description, client_id, issue_type, creation_date):
        issue_data = set_issue_data(description, client_id, issue_type, creation_date)
        try:
            self.create_new_issue(issue_data)
        except Exception as e:
            raise JiraException
