from jira import JIRA


# Replace with your Jira instance URL and Personal Access Token (PAT)
class JiraInstance:

    def __init__(self):
        self.host = "<JIRA_BASE_URL>"
        self.pat = "<YOUR-PERSONAL-ACCESS-TOKEN>"
        headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
        headers["Authorization"] = f"Bearer {self.pat}"
        jira = JIRA(server=self.host, options={"headers": headers})
        self.jira = jira

    def create_issue(self, issue_data):
        # issue_data = {
        #     "project": {"key": "<YOUR_PROJECT_KEY>"},
        #     "summary": "New issue created via Python",
        #     "description": "This is a sample issue created using Python script.",
        #     "issuetype": {"name": "Task"},
        # }
        try:
            # Create the issue
            new_issue = self.jira.create_issue(fields=issue_data)

            # Print the key of the created issue
            print("Issue created successfully!")
            print("Issue Key:", new_issue.key)
        except Exception as e:
            print("Failed to create issue:", str(e))
