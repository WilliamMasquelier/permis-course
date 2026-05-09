#!/usr/bin/env bash
# Permis Côtier — one-shot setup for a fresh machine
# Run: bash install.sh

set -euo pipefail

echo ""
echo "=== Permis Côtier — Installation ==="
echo ""

# 1. Install uv if missing
if ! command -v uv &>/dev/null; then
    echo "→ Installation de uv (gestionnaire Python)..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Add uv to PATH for the rest of this script
    export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
    if ! command -v uv &>/dev/null; then
        echo ""
        echo "✗ uv installé mais pas trouvé dans PATH."
        echo "  Ferme ce terminal, rouvre-le, et relance : bash install.sh"
        exit 1
    fi
    echo "✓ uv installé"
else
    echo "✓ uv déjà présent ($(uv --version))"
fi

# 2. Install Python 3.13 if missing (uv manages it automatically)
echo "→ Vérification de Python 3.13..."
uv python install 3.13 2>/dev/null || true
echo "✓ Python 3.13 disponible"

# 3. Create venv and install dependencies
echo "→ Installation des dépendances Python..."
uv sync --no-dev
echo "✓ Dépendances installées (jinja2, markdown-it-py, fsrs)"

# 4. Quick smoke test
echo "→ Vérification rapide..."
.venv/bin/python -c "import jinja2, markdown_it, fsrs; print('✓ Imports OK')"

# 5. Verify rendered outputs exist
if [ -f "output/permis-cours-complet.html" ]; then
    echo "✓ Cours complet présent (output/permis-cours-complet.html)"
else
    echo "→ Génération du cours HTML..."
    .venv/bin/python scripts/render_complete.py
    .venv/bin/python scripts/render_course.py
    echo "✓ Cours généré"
fi

echo ""
echo "=== Installation terminée ==="
echo ""
echo "  Lance Claude Code dans ce dossier, puis tape :"
echo "  /permis-tutor   → pour commencer une leçon"
echo "  /permis-setup   → pour vérifier l'installation"
echo ""
