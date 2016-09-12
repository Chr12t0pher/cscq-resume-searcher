import html
import praw
from prawoauth2 import PrawOAuth2Mini
from app import db
from app.models import Comments, Keywords
from secret import secret

r = praw.Reddit(user_agent="/u/Chr12t0pher scraping /r/cscareerquestions [v0.0.1]")
oauth = PrawOAuth2Mini(r, app_key=secret["app_key"], app_secret=secret["app_secret"],
                       access_token=secret["access_token"], refresh_token=secret["refresh_token"], scopes=["read"])
r.config.api_request_delay = 1

posts = r.search("Resume Advice Thread author:alanbot OR author:automoderator", subreddit="cscareerquestions",
                 limit=None, sort="new")

count = 1

for post in posts:
    for comment in post.comments:
        if not comment.author:
            author = "[deleted]"
        else:
            author = comment.author.name
        new_comment = Comments(reddit_id=comment.name[3:], reddit_post_id=comment.link_id[3:],
                               reddit_user=author, text=comment.body, html=html.unescape(comment.body_html),
                               url=post.url+comment.name[3:])
        db.session.add(new_comment)
        print("Added post by /u/" + author)
    db.session.commit()
    print("Committed all top-level posts for this post. {} posts done.".format(count))
    count += 1

print("Setting keywords...")

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["freshman", "first year", "1st year", "starting college",
                                               "starting uni"]):
        new = Keywords(post_id=comment.id, keyword="university:first-year")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["sophomore", "second year", "2nd year"]):
        new = Keywords(post_id=comment.id, keyword="university:second-year")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["junior", "third year", "3rd year"]):
        new = Keywords(post_id=comment.id, keyword="university:third-year")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["senior", "forth year", "4th year", "final year", "graduating",
                                               "last year"]):
        new = Keywords(post_id=comment.id, keyword="university:fourth_final-year")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["london"]):
        new = Keywords(post_id=comment.id, keyword="location:london")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["england", "uk", "great britain", "united kingdom", "northern ireland"]):
        new = Keywords(post_id=comment.id, keyword="location:united-kingdom")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["sf", "san fran", "bay area", "silicon valley", "mountain view"]):
        new = Keywords(post_id=comment.id, keyword="location:san-francisco-bay-area")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["nyc", "new york", "manhattan", "new-york"]):
        new = Keywords(post_id=comment.id, keyword="location:new-york")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["germany", "berlin", "france", "paris", "belgium", "brussels", "denmark",
                                               "copenhagen", "finland", "helsinki", "ireland", "dublin", "netherlands",
                                               "amsterdam", "holland", "norway", "oslo", "poland", "warsaw", "spain",
                                               "madrid", "sweden", "stockholm", "switzerland", "bern"]):
        new = Keywords(post_id=comment.id, keyword="location:europe")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["connecticut", "vermont", "illinois", "rhode island", "america", "usa"
                                               "hawaii", "colorado", "arizona", "new jersey", "tennessee", "florida",
                                               "north carolina", "palau", "american samoa", "oregon", "virginia",
                                               "new hampshire", "idaho", "indiana", "iowa", "utah", "kansas",
                                               "new mexico", "south carolina", "north dakota", "montana", "wyoming",
                                               "maine", "arkansas", "louisiana", "texas", "maryland", "ohio",
                                               "south dakota", "california", "michigan", "pennsylvania", "minnesota",
                                               "washington", "nebraska", "mississippi", "oklahoma", "new york",
                                               "nevada", "kentucky", "alaska", "delaware", "alabama", "wisconsin",
                                               "georgia", "missouri", "west virginia", "massachusetts", "columbia",
                                               "los angeles", "nyc", "chicago", "houston", "philadeplphia", "phoenix",
                                               "san diego", "dallas", "san jose", "austin", "san francisco", "seattle",
                                               "denver", "boston", "las vegas", "atlanta"]):
        new = Keywords(post_id=comment.id, keyword="location:united-states")
        db.session.add(new)
db.session.commit()

for comment in Comments.query.all():
    if any(x in comment.text.lower() for x in ["experienced", "current job", " employed", "working at"]):
        new = Keywords(post_id=comment.id, keyword="experienced")
        db.session.add(new)
db.session.commit()

