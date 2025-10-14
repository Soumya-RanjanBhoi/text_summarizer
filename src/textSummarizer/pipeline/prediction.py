from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from textSummarizer.config.configuration import ConfriguationManager

class PredictionPipelines:
    def __init__(self):
        self.config = ConfriguationManager()

        eval_config = self.config.get_model_evaluation_config()
        translation_config = self.config.get_model_translation_config()

        self.summarizer_tokenizer = AutoTokenizer.from_pretrained(eval_config.model_path)
        self.summarizer_model = AutoModelForSeq2SeqLM.from_pretrained(eval_config.model_path)

        self.translation_tokenizer = AutoTokenizer.from_pretrained(translation_config.tokenizer_path)
        self.translation_model = AutoModelForSeq2SeqLM.from_pretrained(translation_config.model_path)

        self.summarizer_pipe = pipeline(
            "summarization", model=self.summarizer_model, tokenizer=self.summarizer_tokenizer
        )
        self.trans_pipe = pipeline(
            "translation", model=self.translation_model, tokenizer=self.translation_tokenizer,
            max_length=1024, truncation=True
        )

    def summarize(self, text, text_len):

        gen_kwargs = {
        "num_beams": 4,
        "max_length": text_len,
        "min_length": int(text_len * 0.6),
        "length_penalty": 0.9,
        "early_stopping": True,
        "truncation": False
    }

        output = self.summarizer_pipe(text, **gen_kwargs)[0]['summary_text']
        return output

    def translate(self, text):
        output = self.trans_pipe(text)[0]['translation_text']
        return output
