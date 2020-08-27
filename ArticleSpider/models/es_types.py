# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    #伯乐在线文章类型
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"

class ZhihuQuestionType(DocType):
    #知乎问题类型
    suggest = Completion(analyzer=ik_analyzer)
    zhihu_id = Integer()

    title = Text(analyzer="ik_max_word")
    create_time = Date()
    update_time = Date()
    crawl_time = Date()
    crawl_update_time = Date()
    url = Keyword()
    answer_num = Integer()
    comments_num = Integer()
    watch_user_num = Integer()
    click_num = Integer()
    topics = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "question"
        doc_type = "question"

class ZhihuAnswerType(DocType):
    #知乎回答类型
    suggest = Completion(analyzer=ik_analyzer)
    zhihu_id = Integer()
    question_id = Integer()
    author_id = Keyword()
    create_time = Date()
    update_time = Date()
    crawl_time = Date()
    crawl_update_time = Date()
    url = Keyword()
    praise_num = Integer()
    comments_num = Integer()
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "answer"
        doc_type = "answer"

if __name__ == "__main__":
    ArticleType.init()
    # ZhihuQuestionType.init()
    # ZhihuAnswerType.init()
