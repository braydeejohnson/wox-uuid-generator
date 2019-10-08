# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import uuid
import pyperclip
from services.Application import Application

app = Application()


class Uuid(Wox):

    def query(self, query):
        results = []
        _uuid = "{}".format(uuid.uuid4())
        results.append({
            "Title": "Uuid Generator",
            "SubTitle": _uuid,
            "IcoPath": "Images/app.ico",
            "ContextData": _uuid,
            'JsonRPCAction': {
                'method': 'copy_clip',
                'parameters': [_uuid],
                'dontHideAfterAction': True
            }
        })
        return results

    def copy_clip(self, query):
        pyperclip.copy(query)
        WoxAPI.hide_app()

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath": "Images/app.ico"
        })
        return results


if __name__ == "__main__":
    Uuid()
