from langchain_openai import (
    ChatOpenAI,
)  # 用 OpenAI 兼容接口和模型对话（阿里云等也兼容这个接口）
import os  # Python 自带：用来读「环境变量」（如 API 密钥）

# load_dotenv：从项目根目录的 .env 文件里，把变量加载到「环境」里，之后用 os.getenv("变量名") 就能读到。
# 把密钥写在 .env 里而不是代码里，既安全（不把密钥提交到 Git），又方便换环境（开发/生产用不同 .env）。
from dotenv import load_dotenv

# LangChainException：LangChain 在调用模型失败时会抛出的异常类型。
# 在 main() 里用 except LangChainException 单独接住这类错误，就能打出「模型调用失败」的日志，和配置错误、其他未知错误区分开。
from langchain_core.exceptions import LangChainException
from openai import base_url

# 真正执行「从 .env 加载到环境」；encoding='utf-8' 避免 .env 里有中文时乱码。
load_dotenv(encoding="utf-8")

import logging
_log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, _log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)  # 当前模块的 logger，后面用 logger.info(...) 即可

def init_llm_client() -> ChatOpenAI:
    api_key = os.getenv("KIMI_API_KEY")
    if not api_key:
        raise ValueError("KIMI_API_KEY environment variable not set")

    llm =  ChatOpenAI(
        model="kimi-k3",
        api_key = api_key,
        base_url = "https://api.moonshot.cn/v1",



    )
    return llm

def main():
    try :
        llm = init_llm_client()
        logger.info("LLM客户端初始化成功")

        question = "你是谁"
        response = llm.invoke(question)
        logger.info(f"问题：{question}")
        logger.info(f"回答：{response.content}")

    except ValueError as e:
    # 例如：.env 里没配 QWEN_API_KEY，init_llm_client 里会 raise ValueError
        logger.error(f"配置错误：{str(e)}")

    except LangChainException as e:
    # 例如：网络失败、API 限流、模型返回异常等，LangChain 会抛出 LangChainException
        logger.error(f"模型调用失败：{str(e)}")
    except Exception as e:
    # 其他没预料到的错误都归到这里，避免程序静默崩溃
        logger.error(f"未知错误：{str(e)}")
    print("==================== 以下是流式输出（另一种调用方式）")
    print("*" * 50)
    response_stream = llm.stream("介绍下 langchain，300字以内")
    for chunk in response_stream:
        print(chunk.content, end="")  # end="" 表示不换行，紧挨着打
    print()  # 流式结束后补一个换行，避免和后续输出粘在一起
if __name__ == "__main__":
    main()

