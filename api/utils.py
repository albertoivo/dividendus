from io import BytesIO
import base64


def matplotlib_to_base64(plt):
    """
    Transform a Matplotlib graph to a base 64 url.

    :param plt: The matplotlib graph after plotting it.
    :return: the matplotlib graph in base64.
    """
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = 'data:image/png;base64,{}'.format(figdata_png.decode("utf-8"))

    return result
