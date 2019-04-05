from github import Github
import time

# Authentication for the user to github.com

g = Github("Testask", "Testask84218421")
u = g.get_user()


# test1
# Delete all repositories on github.com
def check_rep():
    count = 0
    for repo in u.get_repos():
        print(repo.name)
        mess = repo.delete()


    repo_count = len([i for i in u.get_repos()])
    print(repo_count)
    while repo_count != 0:
        repo_count = len([i for i in u.get_repos()])

    repo_count = len([i for i in u.get_repos()])

# Create a repository on github.com
    repo = u.create_repo("Elmira")
    time.sleep(30)





def repos_sum():
    repos = u.get_repos()
    assert len([i.name for i in repos]) == 1, "Should be 1"


# test2
# Create an issue on github.com

def create_issue():
    repo = g.get_repo('Testask/Elmira')
    issue = repo.create_issue(title="This is a new issue")
    founded_issue = repo.get_issue(number=issue._number.value)

    #Get list of open issues
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(issue)

    assert issue == founded_issue, "The test with issue creating was not passed"

# test3
# Create a Milestone on github.com

def create_milestone():
    repo = g.get_repo('Testask/Elmira')
    milestone = repo.create_milestone(title='New Milestone')
    created_milestone = repo.get_milestone(number=1)

    # Get milestone list
    open_milestones = repo.get_milestones(state='open')
    for milestone in open_milestones:
        print(milestone)

    assert milestone == created_milestone, "The test with milestone creating was not passed"

# test4
# Create a new file in the repository


def create_new_file():
    repo = g.get_repo('Testask/Elmira')
    repo.create_file("test.txt", "test", "test", branch="test")
    time.sleep(5)
    contents = repo.get_contents("")

#Get list of files
    l = list()
    for content_file in contents:
        l.append(content_file.name)
        print(content_file.name)

    assert l[0] == 'test.txt', "There is an error with list of files"

#test5

if __name__ == "__main__":
    check_rep()
    repos_sum()
    create_issue()
    create_milestone()
    create_new_file()
    print("Everything passed")
