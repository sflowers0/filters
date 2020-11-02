import difflib

def htmldiff(pre_string, post_string, from_desc='pre', to_desc='post'):

    diff = difflib.HtmlDiff(tabsize=3, wrapcolumn=93).make_file(
        pre_string.split('\n'), post_string.split('\n'),
        fromdesc=from_desc, todesc=to_desc, context=True)

    return diff

class FilterModule(object):
    def filters(self):
        return {"htmldiff": htmldiff}
