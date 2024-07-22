import dashing

ui = dashing.HSplit(
        dashing.VSplit(
            dashing.HGauge(val=50, title="foo", border_color=5),
        )
    )
# access a tile by index
gauge = ui.items[0].items[0]
gauge.value = 3.0

# display/refresh the ui
ui.display()