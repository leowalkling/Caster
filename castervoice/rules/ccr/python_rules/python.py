'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Pause, Dictation, Choice

from castervoice.lib.actions import Text, Key
from castervoice.rules.ccr.standard import SymbolSpecs
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R
from castervoice.lib.temporary import Store, Retrieve


class Python(MergeRule):

    mapping = {
        "pie " + SymbolSpecs.IF:
            R(Key("i,f,space,colon,left")),
        "pie " + SymbolSpecs.ELSE:
            R(Text("else:") + Key("enter")),
        # (no switch in Python)
        "pie " + SymbolSpecs.BREAK:
            R(Text("break")),
        "pie " + SymbolSpecs.FOR_EACH_LOOP:
            R(Store() + Text("for  in :") + Key("left:5") +
              Retrieve(action_if_text="right:5")),
        "pie " + SymbolSpecs.FOR_LOOP:
            R(Store() + Text("for i in range(0, ):") + Key("left:2") +
              Retrieve(action_if_text="right:2")),
        "pie " + SymbolSpecs.WHILE_LOOP:
            R(Store() + Text("while :") + Key("left") + Retrieve(action_if_text="right")),
        # (no do-while in Python)
        "pie " + SymbolSpecs.TO_INTEGER:
            R(Store() + Text("int()") + Key("left") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.TO_FLOAT:
            R(Store() + Text("float()") + Key("left") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.TO_STRING:
            R(Store() + Text("str()") + Key("left") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.AND:
            R(Text(" and ")),
        "pie " + SymbolSpecs.OR:
            R(Text(" or ")),
        "pie " + SymbolSpecs.NOT:
            R(Text("!")),
        "pie " + SymbolSpecs.SYSOUT:
            R(Store() + Text("print()") + Key("left") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.IMPORT:
            R(Text("import ")),
        "pie " + SymbolSpecs.FUNCTION:
            R(Store() + Text("def ():") + Key("left:3") +
              Retrieve(action_if_text="right:3")),
        "pie " + SymbolSpecs.CLASS:
            R(Store() + Text("class :") + Key("left") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.COMMENT:
            R(Store() + Text("#") + Key("space") + Retrieve(action_if_text="right")),
        "pie " + SymbolSpecs.LONG_COMMENT:
            R(Store() + Text("''''''") + Key("left:3") +
              Retrieve(action_if_text="right:3")),
        "pie " + SymbolSpecs.NULL:
            R(Text("None")),
        "pie " + SymbolSpecs.RETURN:
            R(Text("return ")),
        # SymbolSpecs.TRUE:
        #     R(Text("True")),
        # SymbolSpecs.FALSE:
        #     R(Text("False")),
        "pie true":
            R(Text("True")),
        "pie false":
            R(Text("False")),

        # Python specific
        "pie iffae":
            R(Text("if ")),
        "pie shells":
            R(Text("else ")),
        "pie from":
            R(Text("from ")),
        "pie self":
            R(Text("self")),
        "pie long not":
            R(Text(" not ")),
        "pie is in":
            R(Text(" in ")),
        "pie (shell iffae | LFA)":
            R(Key("e,l,i,f,space,colon,left")),
        "pie convert to (character | char)":
            R(Store() + Text("chr()") + Key("left") + Retrieve(action_if_text="right")),
        "pie length of":
            R(Store() + Text("len()") + Key("left") + Retrieve(action_if_text="right")),
        "pie global":
            R(Text("global ")),
        "pie assertion":
            R(Text("assert ")),
        "pie list (comprehension | comp)":
            R(Text("[x for x in TOKEN if TOKEN]")),
        # "dot (pie | pi)":
        #     R(Text(".py")),
        # "coding toml":
        #     R(Text("toml")),
        # "coding jason":
        #     R(Text("json")),
        "pie is":
            R(Text(" is ")),
        "pie yield":
            R(Text("yield ")),
        "pie dictionary": R(Text("dict")),

        # Essentially an improved version of the try catch command above
        # probably a better option than this is to use snippets with tab stops
        # VS code has the extension Python-snippets. these are activated by
        # going into the command pallet (cs-p) and typing in "insert snippet"
        # then press enter and then you have choices of snippets show up in the drop-down list.
        # you can also make your own snippets.
        "pie " + "try [<exception>]":
            R(
                Text("try : ") + Pause("10") + Key("enter/2") +
                Text("except %(exception)s:") + Pause("10") + Key("enter/2")),
        "pie " + "try [<exception>] as":
            R(
                Text("try :") + Pause("10") + Key("enter/2") +
                Text("except %(exception)s as :") + Pause("10") + Key("enter/2")),

        # class and class methods
        "pie sub class":
            R(Store() + Text("class ():") + Key("left:3") +
              Retrieve(action_if_text="right:3")),
        "pie dunder":
            R(Store() + Text("____()") + Key("left:4") +
              Retrieve(action_if_text="right:4")),
        "pie init":
            R(Store() + Text("__init__()") + Key("left") +
              Retrieve(action_if_text="right")),
        "pie meth <binary_meth>":
            R(Text("__%(binary_meth)s__(self, other):")),
        "pie meth [<unary_meth>]":
            R(Text("%(unary_meth)s(self):")),
    }

    extras = [
        Dictation("text"),
        Choice("unary_meth", {
            "reper": "__repr__",
            "stir": "__str__",
            "len": "__len__",
        }),
        Choice("binary_meth", {
            "add": "add",
            "subtract": "sub",
        }),
        Choice(
            "exception", {
                "exception": "Exception",
                "stop iteration": "StopIteration",
                "system exit": "SystemExit",
                "standard": "StandardError",
                "arithmetic": "ArithmeticError",
                "overflow": "OverflowError",
                "floating point": "FloatingPointError",
                "zero division": "ZeroDivisionError",
                "assertion": "AssertionError",
                "EOF": "EOFError",
                "import": "ImportError",
                "keyboard interrupt": "KeyboardInterrupt",
                "lookup": "LookupError",
                "index": "IndexError",
                "key": "KeyError",
                "name": "NameError",
                "unbound local": "UnboundLocalError",
                "environment": "EnvironmentError",
                "IO": "IOError",
                "OS": "OSError",
                "syntax": "SyntaxError",
                "system exit": "SystemExit",
                "type": "TypeError",
                "value": "ValueError",
                "run time": "RuntimeError",
                "not implemented": "NotImplementedError",
            })
    ]
    defaults = {"unary_meth": "", "binary_meth": "", "exception": ""}


def get_rule():
    return Python, RuleDetails(ccrtype=CCRType.GLOBAL)
