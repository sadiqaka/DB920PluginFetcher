from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from feeds import fetch_all_feeds
from wordpress import send_draft_to_wordpress

class DB920FetcherScreen(Screen):
    skin = """<screen name="DB920FetcherScreen" position="center,center" size="700,500" title="DB920 Feed Fetcher">
    <widget name="menu" position="10,10" size="680,480" font="Regular;22" />
    </screen>"""

    def __init__(self, session):
        Screen.__init__(self, session)
        self["actions"] = ActionMap(["OkCancelActions"], {
            "ok": self.select_item,
            "cancel": self.close
        }, -1)
        self.items = fetch_all_feeds()
        self.titles = [item['title'] for item in self.items]
        self["menu"] = Label("\n".join([f"{i+1}. {t}" for i, t in enumerate(self.titles)]))
        self.selection = []

    def select_item(self):
        # Minimal example: send all as drafts (improve for real selection)
        for item in self.items:
            send_draft_to_wordpress(item["title"], item.get("summary", ""), item["link"])
        self.session.open(MessageBox, "All items sent to WordPress as drafts.", MessageBox.TYPE_INFO)
        self.close()

def main(session, **kwargs):
    session.open(DB920FetcherScreen)

def Plugins(**kwargs):
    return [
        PluginDescriptor(
            name="DB920 Feed Fetcher",
            description="Fetch RSS/YouTube and send to WP",
            where=PluginDescriptor.WHERE_PLUGINMENU,
            fnc=main
        )
    ]
