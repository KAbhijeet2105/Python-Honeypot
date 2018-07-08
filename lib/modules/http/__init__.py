#!/usr/bin/env python
# -*- coding: utf-8 -*-


def category_configuration():
    """
    category configuration

    Returns:
        JSON/Dict category configuration
    """
    return {
        "virtual_machine_name": "ohp_httpserver",
        "virtual_machine_port_number": 80,
        "virtual_machine_internet_access": False,
        "real_machine_port_number": 80
    }