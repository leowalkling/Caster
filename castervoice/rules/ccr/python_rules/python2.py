from dragonfly import MappingRule

from castervoice.lib.actions import Text, Key
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R


class PythonNon(MappingRule):
    mapping = {
        "pie " + "with":
            R(Text("with ")),
        "pie " + "open file":
            R(Text("open('filename','r') as f:")),
        "pie " + "read lines":
            R(Text("content = f.readlines()")),
        "pie " + "try catch":
            R(
                Text("try:") + Key("enter:2/10, backspace") + Text("except Exception:") +
                Key("enter")),
    }


def get_rule():
    return PythonNon, RuleDetails("python companion")
