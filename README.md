# Graphify synthetic pilot

This repository contains only invented demonstration data for a Graphify installation check. It contains no real customer data, chat histories, credentials, or working project files.

Pilot marker: LANTERN-PILOT-20261112.

The imaginary Lantern shop uses integer cents. `pricing.py` defines `line_total`. `orders.py` imports it and defines `summarize_order`.

Example: two items at 1500 cents and one item at 1300 cents produce a total of 4300 cents.

The pilot is limited to graph indexing, source-linked queries, and an optional explicitly requested synthetic memory check. It does not enable monitoring, schedules, real sales, or paid services.
