-- Render plain ```mermaid fences (GitHub style) as diagrams, so lit-review
-- markdown looks the same on GitHub and on this site.
local function escape(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

function CodeBlock(el)
  if el.classes:includes("mermaid") then
    return pandoc.RawBlock("html", '<pre class="mermaid">' .. escape(el.text) .. "</pre>")
  end
end
