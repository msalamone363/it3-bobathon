# Bob Troubleshooting Guide

Common issues and solutions when working with Bob.

## 🔍 General Troubleshooting

### Issue: Bob Can't Find a File

**Symptoms:**
- Error message about file not found
- Bob says the file doesn't exist

**Solutions:**
1. **Check the path:** Use `list_files` to see the correct path
   ```
   "List all files in the current directory"
   ```

2. **Use relative paths:** Paths should be relative to workspace root
   ```
   ❌ ~/project/src/app.py
   ✅ src/app.py
   ```

3. **Check for typos:** Verify spelling and case sensitivity
   ```
   ❌ src/App.py (wrong case)
   ✅ src/app.py
   ```

---

### Issue: Changes Didn't Apply

**Symptoms:**
- Bob says changes were made but file looks the same
- apply_diff failed to match content

**Solutions:**
1. **Read the file first:** Check current content
   ```
   "Read src/app.py to see the current state"
   ```

2. **Match content exactly:** apply_diff requires exact matches
   ```
   Include proper indentation and spacing
   ```

3. **Use write_to_file for small files:** If apply_diff keeps failing
   ```
   "Rewrite the entire config.json file with the updated values"
   ```

4. **Check line numbers:** Ensure you're editing the right section
   ```
   "Read src/app.py lines 40-60 to see the function I need to update"
   ```

---

### Issue: Bob Seems Confused

**Symptoms:**
- Bob asks for clarification
- Suggestions don't match expectations
- Bob misunderstands the request

**Solutions:**
1. **Provide more context:**
   ```
   ❌ "Fix the bug"
   ✅ "Fix the null pointer exception in getUserData() on line 45"
   ```

2. **Be specific about location:**
   ```
   ❌ "Update the config"
   ✅ "Update the timeout value in config/settings.json"
   ```

3. **Explain the goal:**
   ```
   "I need to add email validation to prevent invalid emails from being saved"
   ```

4. **Show examples:**
   ```
   "Add validation similar to how we validate passwords in the User model"
   ```

---

### Issue: Command Execution Failed

**Symptoms:**
- Command returns error
- Tests fail unexpectedly
- Build errors

**Solutions:**
1. **Check command syntax:**
   ```
   ❌ "Run tests"
   ✅ "Run pytest tests/"
   ```

2. **Verify environment:**
   ```
   "Check if pytest is installed: pip list | grep pytest"
   ```

3. **Check working directory:**
   ```
   "Run: cd backend && pytest tests/"
   ```

4. **Review error messages:**
   ```
   "Explain this error message: [paste error]"
   ```

---

## 🐛 Code-Specific Issues

### Issue: Tests Failing After Changes

**Symptoms:**
- Tests passed before, fail now
- Unexpected test failures

**Solutions:**
1. **Review what changed:**
   ```
   "Show me what changed in the last edit"
   ```

2. **Run specific test:**
   ```
   "Run just the failing test: pytest tests/test_user.py::test_email_validation"
   ```

3. **Check test expectations:**
   ```
   "Read the failing test and explain what it expects"
   ```

4. **Revert if needed:**
   ```
   "Undo the last change to src/user.py"
   ```

---

### Issue: Import Errors

**Symptoms:**
- ModuleNotFoundError
- ImportError
- Circular import issues

**Solutions:**
1. **Check import paths:**
   ```
   "Search for how other files import from this module"
   ```

2. **Verify module structure:**
   ```
   "List all Python files and show me the package structure"
   ```

3. **Check __init__.py files:**
   ```
   "Read the __init__.py files in the package"
   ```

4. **Fix import statements:**
   ```
   "Update the import to use: from src.utils import helper"
   ```

---

### Issue: Syntax Errors

**Symptoms:**
- Code won't run
- Syntax error messages
- Indentation errors

**Solutions:**
1. **Read the problematic section:**
   ```
   "Read src/app.py lines 40-50 where the syntax error is"
   ```

2. **Check indentation:**
   ```
   "Fix the indentation in the calculate_total function"
   ```

3. **Validate syntax:**
   ```
   "Check if this code has any syntax errors: [paste code]"
   ```

4. **Use linter:**
   ```
   "Run pylint on src/app.py to check for issues"
   ```

---

## 🔧 Tool-Specific Issues

### Issue: apply_diff Not Working

**Symptoms:**
- "Could not find match" error
- Changes not applied

**Solutions:**
1. **Read before editing:**
   ```
   "Read the file first so you can see the exact content"
   ```

2. **Include enough context:**
   ```
   Include a few lines before and after the change
   ```

3. **Match whitespace exactly:**
   ```
   Pay attention to spaces vs tabs
   ```

4. **Use write_to_file instead:**
   ```
   For small files, rewrite the entire file
   ```

---

### Issue: read_file Shows Too Much

**Symptoms:**
- File is very large
- Too much output
- Hard to find relevant section

**Solutions:**
1. **Use line ranges:**
   ```
   "Read src/app.py lines 100-150"
   ```

2. **Read multiple ranges:**
   ```
   "Read src/app.py lines 1-20 and 100-120"
   ```

3. **Search first:**
   ```
   "Search for the function definition, then read that section"
   ```

---

### Issue: search_files Returns Too Many Results

**Symptoms:**
- Hundreds of matches
- Hard to find relevant results

**Solutions:**
1. **Use more specific regex:**
   ```
   ❌ "Search for 'user'"
   ✅ "Search for 'def.*user.*email' to find user email functions"
   ```

2. **Limit to specific directories:**
   ```
   "Search in src/models/ only"
   ```

3. **Use file patterns:**
   ```
   "Search for TODO in *.py files only"
   ```

---

## 💻 Environment Issues

### Issue: Bob Can't Access Files

**Symptoms:**
- Permission denied errors
- Can't read/write files

**Solutions:**
1. **Check file permissions:**
   ```
   "Run: ls -la src/app.py"
   ```

2. **Verify workspace directory:**
   ```
   "What is the current workspace directory?"
   ```

3. **Check if file is open elsewhere:**
   ```
   Close the file in other editors
   ```

---

### Issue: Commands Not Found

**Symptoms:**
- "command not found" errors
- Tools not available

**Solutions:**
1. **Check if tool is installed:**
   ```
   "Run: which pytest"
   ```

2. **Install missing tools:**
   ```
   "Run: pip install pytest"
   ```

3. **Use full path:**
   ```
   "Run: /usr/local/bin/python -m pytest"
   ```

4. **Activate virtual environment:**
   ```
   "Run: source venv/bin/activate && pytest"
   ```

---

## 🎯 Performance Issues

### Issue: Bob is Slow

**Symptoms:**
- Long wait times
- Timeouts

**Solutions:**
1. **Read smaller sections:**
   ```
   Use line ranges instead of reading entire large files
   ```

2. **Be more specific:**
   ```
   Narrow down the scope of searches
   ```

3. **Break into smaller tasks:**
   ```
   Do one thing at a time instead of complex multi-step operations
   ```

---

### Issue: Too Many Tool Uses

**Symptoms:**
- Bob makes many requests
- Takes long time to complete

**Solutions:**
1. **Provide more context upfront:**
   ```
   "Read these 3 files together: [list files]"
   ```

2. **Be more specific:**
   ```
   Tell Bob exactly what you want instead of asking it to figure it out
   ```

3. **Combine related operations:**
   ```
   "Make these 3 changes in one request: [list changes]"
   ```

---

## 🤔 Understanding Issues

### Issue: Bob's Suggestion Doesn't Make Sense

**Symptoms:**
- Unexpected code changes
- Doesn't match requirements

**Solutions:**
1. **Clarify requirements:**
   ```
   "Let me clarify: I need [specific requirement]"
   ```

2. **Provide examples:**
   ```
   "Here's an example of what I want: [example]"
   ```

3. **Ask for explanation:**
   ```
   "Why did you suggest this approach?"
   ```

4. **Request alternatives:**
   ```
   "Show me 2-3 different ways to solve this"
   ```

---

### Issue: Bob Asks Too Many Questions

**Symptoms:**
- Bob keeps asking for clarification
- Can't proceed without more info

**Solutions:**
1. **Provide complete context:**
   ```
   Include: what, where, why, and any constraints
   ```

2. **Show examples:**
   ```
   Reference similar code in the project
   ```

3. **Be specific about location:**
   ```
   Exact file paths and line numbers
   ```

---

## 📋 Best Practices to Avoid Issues

### 1. Always Read Before Editing
```
"Read src/app.py, then update the timeout value"
```

### 2. Verify Changes
```
"Make the change, then run tests to verify"
```

### 3. Provide Context
```
"I'm trying to [goal] because [reason]. Update [file] to [specific change]"
```

### 4. Break Down Complex Tasks
```
"Let's do this in steps:
1. First, read the current implementation
2. Then, update the function
3. Finally, add tests"
```

### 5. Use Version Control
```
Commit working code before making changes
```

---

## 🆘 When All Else Fails

### 1. Start Fresh
- Restart Bob
- Clear context
- Try a simpler approach

### 2. Ask for Help
- Consult facilitator
- Check documentation
- Ask in support channel

### 3. Manual Intervention
- Make the change manually
- Ask Bob to review it
- Continue from there

### 4. Simplify
- Break into smaller pieces
- Do one thing at a time
- Build up gradually

---

## 📞 Getting Support

### During the Bob-a-thon
- **Ask your IBM facilitator** — Mat Davis, Daniel Fleck, or Walt Perez are on-site at both locations
- Pair with another participant and work through it together
- Check `resources/external-links.md` for Python/pandas documentation

### After the Bob-a-thon
- **Email:** madison.ramsey@ibm.com
- **Bob documentation:** https://ibm.biz/bob-doc
- **Office hours:** Week of Sep 29 (TBD — Madison will send invite)

---

## 💡 Pro Tips

1. **Keep prompts clear and specific**
2. **Always verify changes with tests**
3. **Read files before modifying them**
4. **Use version control for safety**
5. **Break complex tasks into steps**
6. **Provide context and examples**
7. **Don't hesitate to ask Bob to explain**

---

**Remember:** Most issues can be resolved by being more specific and providing better context!