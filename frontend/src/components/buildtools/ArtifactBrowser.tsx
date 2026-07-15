"use client";
import { useState } from "react";
import { Folder, FileCode, Download, TrendingUp, TrendingDown, Minus, ChevronDown, ChevronRight, Archive } from "lucide-react";

type ArtifactNode = {
  name: string; type: "dir" | "file"; size?: string; delta?: number; modified?: string;
  children?: ArtifactNode[]; expanded?: boolean;
};

const ARTIFACT_TREE: ArtifactNode[] = [
  {
    name:"target/", type:"dir", expanded:true, children:[
      {
        name:"release/", type:"dir", expanded:true, children:[
          { name:"determinex-core.exe",   type:"file", size:"12.4 MB", delta:0.2,  modified:"14:32:04" },
          { name:"determinex-core.d",     type:"file", size:"0.1 MB",  delta:0,    modified:"14:32:04" },
          { name:"determinex-core.pdb",   type:"file", size:"4.2 MB",  delta:0,    modified:"14:32:04" },
        ],
      },
      {
        name:"debug/", type:"dir", expanded:false, children:[
          { name:"determinex-core.exe",   type:"file", size:"68.1 MB", delta:-1.2, modified:"13:15:22" },
        ],
      },
    ],
  },
  {
    name:"frontend/.next/", type:"dir", expanded:true, children:[
      { name:"static/",               type:"dir",  size:"4.2 MB",  delta:0.3,  modified:"14:45:18" },
      { name:"server/",               type:"dir",  size:"1.8 MB",  delta:0.1,  modified:"14:45:18" },
      { name:"BUILD_ID",              type:"file", size:"0.0 KB",  delta:0,    modified:"14:45:18" },
    ],
  },
  {
    name:"dist/", type:"dir", expanded:false, children:[
      { name:"determinex-0.1.0-setup.exe", type:"file", size:"98.4 MB", delta:1.2, modified:"yesterday" },
      { name:"determinex-0.1.0.tar.gz",    type:"file", size:"44.1 MB", delta:0.8, modified:"yesterday" },
    ],
  },
  {
    name:"corpus/programbench/", type:"dir", expanded:false, children:[
      { name:"locked/",               type:"dir",  size:"2.1 GB",  delta:45.2, modified:"today" },
      { name:"training_corpus/",      type:"dir",  size:"380 MB",  delta:12.1, modified:"today" },
    ],
  },
];

function DeltaIcon({ delta }: { delta?: number }) {
  if (!delta || delta === 0) return <Minus size={9} className="text-gray-700" />;
  return delta > 0
    ? <TrendingUp size={9} className="text-amber-400" />
    : <TrendingDown size={9} className="text-emerald-400" />;
}

function TreeNode({ node, depth = 0, onToggle }: { node: ArtifactNode; depth?: number; onToggle: (n: ArtifactNode) => void }) {
  const indent = depth * 16;
  if (node.type === "dir") {
    return (
      <div>
        <button onClick={() => onToggle(node)}
          className="flex items-center gap-2 w-full px-4 py-1.5 hover:bg-white/[0.02] transition-colors text-left"
          style={{ paddingLeft: `${16 + indent}px` }}>
          {node.expanded ? <ChevronDown size={11} className="text-gray-600 shrink-0" /> : <ChevronRight size={11} className="text-gray-600 shrink-0" />}
          <Folder size={12} className="text-amber-500/60 shrink-0" />
          <span className="text-[10px] font-mono text-gray-400 flex-1">{node.name}</span>
          {node.size && <span className="text-[9px] font-mono text-gray-600">{node.size}</span>}
        </button>
        {node.expanded && node.children?.map((child, i) => (
          <TreeNode key={i} node={child} depth={depth + 1} onToggle={onToggle} />
        ))}
      </div>
    );
  }
  return (
    <div className="group flex items-center gap-2 px-4 py-1.5 hover:bg-white/[0.02] transition-colors"
      style={{ paddingLeft: `${16 + indent}px` }}>
      <FileCode size={11} className="text-gray-600 shrink-0" />
      <span className="text-[10px] font-mono text-gray-500 flex-1 truncate">{node.name}</span>
      <div className="flex items-center gap-2 shrink-0">
        <DeltaIcon delta={node.delta} />
        {node.size && <span className="text-[9px] font-mono text-gray-600">{node.size}</span>}
        <span className="text-[8px] text-gray-700">{node.modified}</span>
        <button className="opacity-0 group-hover:opacity-100 text-gray-700 hover:text-gray-400 transition-all p-1">
          <Download size={10} />
        </button>
      </div>
    </div>
  );
}

export function ArtifactBrowser() {
  const [tree, setTree] = useState(ARTIFACT_TREE);

  const toggleNode = (target: ArtifactNode) => {
    const toggle = (nodes: ArtifactNode[]): ArtifactNode[] =>
      nodes.map((n) => n === target ? { ...n, expanded: !n.expanded } : { ...n, children: n.children ? toggle(n.children) : undefined });
    setTree(toggle(tree));
  };

  const totalSize = "2.7 GB";

  return (
    <div className="flex h-full flex-col overflow-hidden">
      <div className="shrink-0 flex items-center gap-3 border-b px-4 py-2.5" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        <Archive size={12} className="text-gray-600" />
        <span className="text-[9px] uppercase font-black tracking-widest text-gray-600">Build Artifacts</span>
        <span className="ml-auto text-[9px] font-mono text-gray-700">{totalSize} total</span>
        <div className="flex items-center gap-1 text-[8px] text-gray-700 ml-2">
          <TrendingUp size={9} className="text-amber-400" /> = larger
          <TrendingDown size={9} className="text-emerald-400 ml-2" /> = smaller
        </div>
      </div>

      <div className="flex-1 overflow-y-auto no-scrollbar py-2">
        {tree.map((node, i) => (
          <TreeNode key={i} node={node} onToggle={toggleNode} />
        ))}
      </div>
    </div>
  );
}
