import functools
import logging
import os
import os.path

from jinja2 import Environment, FileSystemLoader

import flash_gradio


@functools.lru_cache
def _get_env():
    return Environment(loader=FileSystemLoader(flash_gradio.TEMPLATES_ROOT))


def generate_script(
    path,
    template_file,
    **kwargs,
):
    template = _get_env().get_template(os.path.join(template_file))

    variables = dict(
        root=os.path.dirname(path),
        **kwargs,
    )

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        logging.info(f"Rendering {template_file} with variables: {variables}")
        f.write(template.render(**variables))
