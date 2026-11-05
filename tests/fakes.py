"""Hand-written fakes of the Selenium driver and elements."""

from typing import Any

from selenium.common.exceptions import ElementClickInterceptedException


class FakeElement:
    def __init__(
        self, intercepted: bool = False, children: list["FakeElement"] | None = None
    ) -> None:
        self.intercepted = intercepted
        self.children = children or []
        self.clicks = 0
        self.typed: list[str] = []

    def click(self) -> None:
        if self.intercepted:
            raise ElementClickInterceptedException("blocked")
        self.clicks += 1

    def send_keys(self, text: str) -> None:
        self.typed.append(text)

    def find_elements(self, by: str, value: str) -> list["FakeElement"]:
        return self.children


class FakeDriver:
    def __init__(self, present: dict[str, list[FakeElement]]) -> None:
        self.present = present
        self.visited: list[str] = []
        self.scripts: list[tuple[str, Any]] = []
        self.quit_calls = 0

    def quit(self) -> None:
        self.quit_calls += 1

    def get(self, url: str) -> None:
        self.visited.append(url)

    def find_elements(self, by: str, value: str) -> list[FakeElement]:
        return self.present.get(value, [])

    def find_element(self, by: str, value: str) -> FakeElement:
        found = self.find_elements(by, value)
        if not found:
            raise LookupError(value)
        return found[0]

    def execute_script(self, script: str, *args: Any) -> None:
        self.scripts.append((script, args[0]))
