from flash_gradio import FlashGradio

from unittest import mock
from unittest.mock import ANY


@mock.patch("flash_gradio.component.gradio")
def test_flash_gradio_text_classification(gradio_mock):
    checkpoint_path = "checkpoint.ckpt"

    # Sample run data config to test workflow
    run_dict = {
        "task": "text_classification",
        "url": "https://pl-flash-data.s3.amazonaws.com/imdb.zip",
        "data_config": {
            "target": "from_csv",
            "input_field": "review",
            "target_fields": "sentiment",
            "train_file": "imdb/train.csv",
            "val_file": "imdb/valid.csv",
        },
    }

    flash_gradio = FlashGradio()
    flash_gradio.run(
        run_dict["task"],
        run_dict["url"],
        run_dict["data_config"],
        checkpoint_path,
    )
    gradio_mock.Interface.assert_called_once_with(
        fn=ANY,
        inputs=ANY,
        outputs=ANY
    )
