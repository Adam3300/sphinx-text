import re
from sphinx.directives.other import TocTree

def setup(app):
    app.add_directive('toctree-filt', TocTreeFilt)
    return {'version': '1.0.0', 'parallel_read_safe': True}

class TocTreeFilt(TocTree):
    hasPat = re.compile(r'^\s*:(.+):(.+)$')

    def filter_entries(self, entries, env):
        tags = env.app.tags
        filtered = []
        for e in entries:
            m = self.hasPat.match(e)
            if m:
                tag, entry = m.groups()
                # Include the entry if the tag is set in the build tags
                if tag in tags:
                    filtered.append(entry)
                # Exclude the entry if the tag is 'onprem' or 'saas' and it's not in the build tags
                elif tag in ['onprem', 'saas'] and tag not in tags:
                    continue
            else:
                filtered.append(e)
        return filtered

    def run(self):
        env = self.state.document.settings.env
        # Remove all TOC entries that should not be on display
        self.content = self.filter_entries(self.content, env)
        return super().run()
