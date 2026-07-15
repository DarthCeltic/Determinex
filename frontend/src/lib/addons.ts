export type AddonStatus = "installed" | "available" | "beta" | "builtin";
export type AddonCategory = "llm" | "oracle" | "benchmark" | "privacy" | "integration" | "theme";

export type Addon = {
  id: string;
  name: string;
  author: string;
  category: AddonCategory;
  description: string;
  version: string;
  status: AddonStatus;
  icon: string;
  tags: string[];
  featured?: boolean;
};

export const ADDONS: Addon[] = [
  // LLM Providers
  { id:"anthropic", name:"Anthropic Claude",    author:"Anthropic",           category:"llm",         description:"Claude Opus 4.8 · Sonnet 4.6 · Haiku 4.5. Best reasoning + code generation.",  version:"4.8.0",  status:"builtin",   icon:"🤖", tags:["cloud","reasoning","code"], featured:true },
  { id:"deepseek",  name:"DeepSeek V4",         author:"DeepSeek AI",         category:"llm",         description:"Frontier open-source model. Powers the default Builder in SWE-bench configs.",  version:"4.0.1",  status:"installed", icon:"🔵", tags:["cloud","code","fast"]        },
  { id:"chatgpt",   name:"ChatGPT",             author:"OpenAI",              category:"llm",         description:"Fallback when Anthropic quota exceeded. Best for complex multi-step reasoning.", version:"5.5.0",  status:"installed", icon:"🟢", tags:["cloud","reasoning"]          },
  { id:"gemini",    name:"Google Gemini 3.1",   author:"Google DeepMind",     category:"llm",         description:"Gemini 3.1 Pro Preview. Strong at UI/UX, visual reasoning, Python AI.",        version:"3.1.0",  status:"available", icon:"🔷", tags:["cloud","multimodal"]         },
  { id:"ollama",    name:"Ollama Local",         author:"Ollama",              category:"llm",         description:"Run Determinex fine-tuned models (C1/C3/C7) and Qwen2.5-Coder locally.",          version:"0.5.4",  status:"installed", icon:"🦙", tags:["local","private","offline"], featured:true },
  { id:"mistral",   name:"Mistral AI",           author:"Mistral",             category:"llm",         description:"C7 Sentinel base. Fast European-sovereign cloud option.",                       version:"7.2.0",  status:"available", icon:"🌀", tags:["cloud","eu-sovereign"]       },
  // Oracles
  { id:"rust-oracle",   name:"Rust / Cargo",     author:"Determinex Core",  category:"oracle", description:"rustc + cargo check + cargo test. The gold standard oracle. All PB Rust tools.", version:"1.83.0", status:"builtin",   icon:"🦀", tags:["rust","compiled","strict"], featured:true },
  { id:"go-oracle",     name:"Go Build",          author:"Determinex Core",  category:"oracle", description:"go build + go test. 100% reproducible. Powers revive, direnv, fzf, trdsql.",    version:"1.22.3", status:"builtin",   icon:"🐹", tags:["go","compiled"]  },
  { id:"python-oracle", name:"Python pytest",     author:"Determinex Core",  category:"oracle", description:"pytest + mypy. Handles TUI, tmux, PTY tests. eureka, keifu, fasttext.",          version:"3.11.9", status:"builtin",   icon:"🐍", tags:["python","dynamic"] },
  { id:"ts-oracle",     name:"TypeScript / tsc",  author:"Determinex Core",  category:"oracle", description:"tsc strict + jest. Frontend oracle. Powers the IDE itself.",                    version:"5.4.2",  status:"builtin",   icon:"📘", tags:["typescript","compiled"] },
  { id:"kotlin-oracle", name:"Kotlin / Gradle",   author:"Community",     category:"oracle", description:"gradle test. JVM oracle for Android + backend Kotlin targets.",                  version:"2.0.0",  status:"available", icon:"🅺", tags:["kotlin","jvm"]   },
  { id:"swift-oracle",  name:"Swift / XCTest",    author:"Community",     category:"oracle", description:"swift test. iOS/macOS oracle. Requires Xcode toolchain.",                        version:"5.10.0", status:"available", icon:"🐦", tags:["swift","apple"]  },
  { id:"cpp-oracle",    name:"C/C++ / CMake",     author:"Determinex Core",  category:"oracle", description:"cmake + make + GTest. Handles doxygen, ditaa, cmatrix, FFmpeg.",                version:"3.28.0", status:"installed", icon:"⚙️", tags:["c","cpp","compiled"] },
  // Benchmarks
  { id:"programbench", name:"ProgramBench",       author:"Determinex Core",  category:"benchmark", description:"201-task CLI reimplementation. 0/200 legitimate locks (corrected 2026-06-30). 62 reference archives retained.", version:"2.1.0", status:"builtin",   icon:"📊", tags:["benchmark","cli","official"], featured:true },
  { id:"swebench",     name:"SWE-bench Lite",     author:"Princeton NLP", category:"benchmark", description:"300 GitHub issues. B-Uncloaked: 14.0%. Privacy-sovereign run active.",       version:"1.0.0", status:"installed", icon:"🐛", tags:["benchmark","github","patches"] },
  { id:"humaneval",    name:"HumanEval+",         author:"OpenAI",        category:"benchmark", description:"164 hand-written Python problems. Fast eval for model selection.",            version:"1.0.0", status:"available", icon:"📝", tags:["benchmark","python","generation"] },
  { id:"livecodebench",name:"LiveCodeBench Pro",  author:"LCB Team",      category:"benchmark", description:"Contamination-free. Rolling 6-month window. True generalization signal.",    version:"2.0.0", status:"available", icon:"⚡", tags:["benchmark","live","competition"] },
  { id:"bigcodebench", name:"BigCodeBench",       author:"BigCode",       category:"benchmark", description:"1140 diverse tasks. Better coverage than HumanEval for real use-cases.",     version:"0.1.2", status:"available", icon:"🔬", tags:["benchmark","diverse"]           },
  // Privacy
  { id:"cloak",    name:"Project Cloak",       author:"Determinex Core",  category:"privacy", description:"AST-aware identifier obfuscation. Cloud-bound payloads use x_NNNN tokens; leakage claims require a current Cloak audit.", version:"3.1.0", status:"builtin",   icon:"🎭", tags:["privacy","obfuscation","ast"], featured:true },
  { id:"rosetta",  name:"Rosetta Stone",        author:"Determinex Core",  category:"privacy", description:"MLP encoder/decoder bridging C1/C3/C7 into shared 4096-dim latent space.",           version:"1.0.0", status:"builtin",   icon:"🪨", tags:["latent","communication","mlp"] },
  { id:"hardened", name:"Hardened Runner",      author:"Determinex Core",  category:"privacy", description:"Sandboxed code execution. Workspace-bounded, env-scrubbed, network-denied.",        version:"2.0.0", status:"builtin",   icon:"🏰", tags:["sandbox","security","isolation"] },
  // Integrations
  { id:"github",   name:"GitHub Actions",       author:"GitHub",        category:"integration", description:"PR checks, CI status, issue sync. Watch runs without leaving the IDE.",     version:"2.3.1", status:"available", icon:"🐙", tags:["ci","cd","github"]           },
  { id:"docker",   name:"Docker / Compose",     author:"Docker Inc",    category:"integration", description:"Container management, compose up/down, log streaming. Eval runner integration.", version:"4.0.0", status:"installed", icon:"🐳", tags:["docker","containers"]        },
  { id:"snyk",     name:"Snyk Security",        author:"Snyk",          category:"integration", description:"Real-time vulnerability scanning. Pre-commit + CI gate. OWASP coverage.",    version:"1.12.0",status:"available", icon:"🛡️", tags:["security","sca","sast"]     },
  { id:"jira",     name:"Jira / Linear",        author:"Community",     category:"integration", description:"Link commits to tickets. Transition status from commit messages.",           version:"0.9.2", status:"available", icon:"📋", tags:["project","tracking"]         },
  { id:"slack",    name:"Slack Notifications",  author:"Community",     category:"integration", description:"Push eval results, lock announcements, and gate escalations to Slack.",     version:"0.8.0", status:"beta",      icon:"💬", tags:["notifications","team"]        },
  // Themes
  { id:"redlens",  name:"Red Lens",    author:"Determinex", category:"theme", description:"Deep crimson precision. For the long compile sessions.", version:"1.2.0", status:"installed", icon:"🔴", tags:["dark","red"]    },
  { id:"deepspace",name:"Deep Space",  author:"Determinex", category:"theme", description:"Midnight void with nebula accents.",                     version:"1.4.0", status:"installed", icon:"🌌", tags:["dark","blue"]   },
  { id:"mechbay",  name:"Mech Bay",    author:"Determinex", category:"theme", description:"Industrial amber on gunmetal. Utility-first.",           version:"1.1.0", status:"available", icon:"🤖", tags:["dark","amber"]  },
  { id:"neon",     name:"Neon Grid",   author:"Community", category:"theme", description:"Cyberpunk green on black. Terminal aesthetic.",           version:"2.0.0", status:"available", icon:"💚", tags:["dark","green"]  },
];
