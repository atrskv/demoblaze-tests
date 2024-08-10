from typing import Optional
from typing import Literal
import dotenv
from pydantic_settings import BaseSettings


class Config(BaseSettings):

    context: Literal['local', 'remote'] = 'local'

    base_url: str = 'https://www.demoblaze.com'
    api_url: str = 'https://api.demoblaze.com'

    driver_name: str = 'chrome'
    driver_version: str = '122.0'

    window_width: int = 1920
    window_height: int = 1080

    timeout: float = 4

    selenoid_url: Optional[str] = None
    selenoid_login: Optional[str] = None
    selenoid_pass: Optional[str] = None


config = Config(_env_file=dotenv.find_dotenv(f'config.{Config().context}.env'))
