## 前（后）端汉化步骤

以汉化一个字段 "database sync test" 例:

1. 添加字段 "database sync test"

前端配置如下：

```javascript
import { t, tn } from "@superset-ui/translation";
<Tabs.TabPane tab={t("database sync test")} key="6">
  ...
</Tabs.TabPane>;
```

后端配置如下：

```python
from flask_babel import gettext as __

error_str = __("database sync test")
```

2. 初始化 po 文件（第一次，没有 zh 文件目录时执行），有 zh 文件跳过此步骤：

```shell
# 在项目根目录下执行 (跳过)
# pybabel init -i superset/translations/messages.pot -d superset/translations -l zh
```

3. 提取新字符串，更新主模板文件 `messages.pot`

```shell
# 在项目根目录下执行
pybabel extract -F superset/translations/babel.cfg -o superset/translations/messages.pot -k _ -k __ -k t -k tn -k tct .
```

4. 根据模板文件 `messages.pot` 去更新各类 `messages.po` 语言文件，如: (zh、en、th...)

```shell
# 在项目根目录下执行
# 模糊匹配更新(不推荐使用)
# pybabel update -i superset/translations/messages.pot -d superset/translations --ignore-obsolete

# 保留翻译更新
pybabel update -i superset/translations/messages.pot -d superset/translations --ignore-obsolete --no-fuzzy-matching
```

5. 翻译字段，在文件 `superset/translations/zh/LC_MESSAGES/messages.po` 中找到 `msgid "database sync test"` 替换下面的 `msgstr ""` 为 `msgstr "数据同步测试"`

```
msgid "database sync test"
msgstr ""

# 替换为你需要翻译的内容

msgid "database sync test"
msgstr "数据同步测试"
```

6. 检查是否安装了 `po2json`，安装了跳过此步骤

```shell
# 在前端项目(superset-frontend)根目录下执行
npm install -g po2json
```

7. 生成或更新各类语言的 json 文件

```shell
# 在项目根目录下执行
./scripts/po2json.sh
```

8. 编译翻译文件，生成对应的二进制 `.mo` 文件。这些二进制文件包含了翻译字符串的映射，可以在应用程序中被使用。

```shell
# 在项目根目录下执行
pybabel compile -d superset/translations
```

9. 重启项目

## 备注:

1. 为了统一翻译，前端用`t`、`tn`等函数，后端用`_`、`__`（`gettext`）等函数，函数里包裹的必须是英文字符串

2. 当且仅当只需更新翻译文字时（即只更新 `.po` 文件），只需执行`步骤 6` 及后续步骤。（即发现翻译的不对就去`superset/translations/zh/LC_MESSAGES/messages.po` 找到对应的字符串然后替换成新的翻译）

3. 如果 使用`./scripts/po2json.sh` 生成的 json 文件没有对应的字符串，去 `superset/translations/zh/LC_MESSAGES/messages.po`文件里找到对应的字符串，删除上面的 `#, fuzzy`再重新执行
