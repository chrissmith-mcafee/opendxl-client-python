# -*- coding: utf-8 -*-
################################################################################
# Copyright (c) 2014 McAfee Inc. - All Rights Reserved.
################################################################################

# Run with python -m unittest dxlclient.test.test_callback_manager

from __future__ import absolute_import
import unittest

import dxlclient.callbacks as callbacks
import dxlclient._callback_manager as callback_manager


class MockRequestCallback(callbacks.RequestCallback):
    def on_request(self, request):
        pass


class MockResponseCallback(callbacks.ResponseCallback):
    def on_response(self, response):
        pass


class MockEventCallback(callbacks.EventCallback):
    def on_event(self, event):
        pass


class CallbackManagerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_request_callback_manager_with_valid_callback(self):
        cbm = callback_manager._RequestCallbackManager()
        cbm.add_callback("/test", MockRequestCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=MockRequestCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockRequestCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=MockRequestCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_request_callback_manager_with_invalid_callback(self):
        cbm = callback_manager._RequestCallbackManager()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", MockResponseCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_request_callback_manager_with_double_registration(self):
        cbm = callback_manager._RequestCallbackManager()
        cbm.add_callback("/test", MockRequestCallback)
        cbm.add_callback("/test", MockRequestCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockRequestCallback)
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_request_callback_manager_with_valid_callback_instance(self):
        cbm = callback_manager._RequestCallbackManager()
        cb = MockRequestCallback()
        cbm.add_callback("/test", cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_request_callback_manager_with_invalid_callback_instance(self):
        cbm = callback_manager._RequestCallbackManager()
        cb = MockResponseCallback()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_response_callback_manager_with_valid_callback(self):
        cbm = callback_manager._ResponseCallbackManager()
        cbm.add_callback("/test", MockResponseCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=MockResponseCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockResponseCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=MockResponseCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_response_callback_manager_with_invalid_callback(self):
        cbm = callback_manager._ResponseCallbackManager()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", MockEventCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_response_callback_manager_with_double_registration(self):
        cbm = callback_manager._ResponseCallbackManager()
        cbm.add_callback("/test", MockResponseCallback)
        cbm.add_callback("/test", MockResponseCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockResponseCallback)
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_response_callback_manager_with_valid_callback_instance(self):
        cbm = callback_manager._ResponseCallbackManager()
        cb = MockResponseCallback()
        cbm.add_callback("/test", cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_response_callback_manager_with_invalid_callback_instance(self):
        cbm = callback_manager._ResponseCallbackManager()
        cb = MockEventCallback()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_event_callback_manager_with_valid_callback(self):
        cbm = callback_manager._EventCallbackManager()
        cbm.add_callback("/test", MockEventCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=MockEventCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockEventCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=MockEventCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_event_callback_manager_with_invalid_callback(self):
        cbm = callback_manager._EventCallbackManager()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", MockRequestCallback)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_event_callback_manager_with_double_registration(self):
        cbm = callback_manager._EventCallbackManager()
        cbm.add_callback("/test", MockEventCallback)
        cbm.add_callback("/test", MockEventCallback)
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", MockEventCallback)
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_event_callback_manager_with_valid_callback_instance(self):
        cbm = callback_manager._EventCallbackManager()
        cb = MockEventCallback()
        cbm.add_callback("/test", cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("/test")))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.add_callback(callback=cb)
        self.assertEqual(1, len(cbm.callbacks_by_channel.get("")))
        self.assertEqual(2, len(cbm.callbacks_by_channel))
        cbm.remove_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(1, len(cbm.callbacks_by_channel))
        cbm.remove_callback(callback=cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get(""))
        self.assertEqual(0, len(cbm.callbacks_by_channel))

    def test_event_callback_manager_with_invalid_callback_instance(self):
        cbm = callback_manager._EventCallbackManager()
        cb = MockRequestCallback()
        with self.assertRaises(ValueError):
            cbm.add_callback("/test", cb)
        self.assertEqual(None, cbm.callbacks_by_channel.get("/test"))
        self.assertEqual(0, len(cbm.callbacks_by_channel))
