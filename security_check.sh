#!/bin/bash

# Security Check Script
echo "🔒 Security Check for MathPix LaTeX Extractor"
echo "============================================="

echo ""
echo "📁 Checking file permissions:"
ls -la .env* 2>/dev/null || echo "No .env files found"

echo ""
echo "🔍 Checking .gitignore:"
if grep -q "\.env" .gitignore 2>/dev/null; then
    echo "✅ .env is properly ignored in .gitignore"
else
    echo "❌ .env is NOT in .gitignore!"
fi

echo ""
echo "🔎 Scanning for exposed credentials in code files:"
if grep -r "peter_johnson\|072eccedd5" . --exclude-dir=.git --exclude-dir=.venv --exclude=security_check.sh --exclude=.env 2>/dev/null; then
    echo "❌ Found exposed credentials in files!"
else
    echo "✅ No exposed credentials found in files"
fi

echo ""
echo "📝 Checking .env.example template:"
if [ -f .env.example ]; then
    if grep -q "your_.*_here" .env.example; then
        echo "✅ .env.example contains placeholder values"
    else
        echo "❌ .env.example may contain real credentials!"
    fi
else
    echo "⚠️  .env.example file missing"
fi

echo ""
echo "🛡️ Environment variable security:"
if [ -f .env ]; then
    echo "✅ .env file exists"
    perm=$(stat -c "%a" .env)
    if [ "$perm" = "600" ]; then
        echo "✅ .env has secure permissions (600)"
    else
        echo "❌ .env permissions are too open: $perm"
    fi
else
    echo "❌ .env file missing!"
fi

echo ""
echo "Security check complete!"
