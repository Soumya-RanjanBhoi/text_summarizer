from textSummarizer.config.configuration import ConfriguationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class PredictionPipelines:
    def __init__(self):
        self.config = ConfriguationManager()

    def summarize(self, text, text_len):
        eval_config = self.config.get_model_evaluation_config()
        tokenizer = AutoTokenizer.from_pretrained(eval_config.model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(eval_config.model_path)

        if text_len == 80:
            len_penalty = 2
        elif text_len == 180:
            len_penalty = 1.0
        elif text_len > 300:
            len_penalty = 0.8
        else:
            len_penalty = 1.2

        gen_kwargs = {
            "num_beams": 8,
            "max_length": text_len,
            "min_length": 25,
            "length_penalty": len_penalty,
            "early_stopping": True
        }

        summarizer_pipe = pipeline("summarization", model=model, tokenizer=tokenizer)
        output = summarizer_pipe(text, **gen_kwargs)[0]['summary_text']
        return output

    def translate(self, text):
        translation_config = self.config.get_model_translation_config()
        tokenizer = AutoTokenizer.from_pretrained(translation_config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(translation_config.model_path)

        trans_pipe = pipeline("translation", model=model, tokenizer=tokenizer, max_length=1024, truncation=True)
        output = trans_pipe(text)[0]['translation_text']
        return output
