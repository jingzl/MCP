from mcp.server.fastmcp import FastMCP
from pydantic import Field

# Initialize FastMCP server
mcp = FastMCP("hello-mcp-server", log_level="ERROR")

# 模拟的数据库
user_database = {
    "001": {"name": "张三", "age": 30, "city": "北京"},
    "002": {"name": "李四", "age": 25, "city": "上海"},
    "003": {"name": "王五", "age": 35, "city": "武汉"},
}


@mcp.tool()
async def get_user_info(user_id: str = Field(description="用户ID")) -> str:
    """查询用户信息。当用户需要根据ID查询用户信息时，调用此工具

    Args:
        user_id: 用户ID

    Returns:
        用户信息的字符串描述
    """
    # 从数据库中获取用户信息
    user_info = user_database.get(user_id, None)

    if user_info:
        return f"用户ID：{user_id}\n姓名：{user_info['name']}\n年龄：{user_info['age']}\n城市：{user_info['city']}"
    else:
        return "未找到该用户的信息"


def main():
    print("Hello from mcpserver1!")
    mcp.run()


if __name__ == "__main__":
    main()
