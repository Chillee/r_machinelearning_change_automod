# AWS Lambda script
import praw
import os


def change_link_rules(event, context):
    reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                         client_secret=os.environ['CLIENT_SECRET'],
                         password=os.environ['PASSWORD'],
                         user_agent="r/ml change automoderator",
                         username="programmerChilli")

    wikipage = reddit.subreddit("machinelearning").wiki["config/automoderator"]
    rules = wikipage.content_md.split('---')

    link_rule = """\r\n    type: link submission\r\n    ~domain (ends-with): ".edu"\r\n    ~domain: ["arxiv.org", "openreview.net"]\r\n    action: remove\r\n    comment: Your post was automatically removed, please read the [rules](https://www.reddit.com/r/MachineLearning/about/rules/). **The moderators will not respond to questions regarding this removal unless you suggest which rule you most likely broke.** If you have a beginner related question, visit  /r/MLQuestions or /r/LearnMachineLearning.\r\n"""

    if event['add_rule'] == True and link_rule not in rules:
        rules.insert(1, link_rule)
    else if event['add_rule'] == False and link_rule in rules:
        rules.remove(link_rule)
    else:
        assert(false)

    wikipage.edit(content='---'.join(rules))
    return {
        'statusCode': 200,
        'body': 'added rule' if event['add_rule'] else 'removed rule'
    }
