from __future__ import annotations


class NotAVariableType:
    """A type the templating system knows nothing about."""

    def __repr__(self):
        return "<NotAVariableType>"


def make_unknown(_value):
    """Return an instance of a type unknown to the template engine."""
    return NotAVariableType()


class FilterModule(object):

    def filters(self):
        return {
            'make_unknown': make_unknown,
        }
