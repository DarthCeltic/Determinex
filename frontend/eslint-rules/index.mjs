import { collectVoidCommands, DEFAULT_TAURI_SRC } from "./voidCommands.mjs";

/**
 * Determinex's local ESLint rules.
 *
 * One rule so far, and it exists because the audit that declared this defect
 * class "fixed" was wrong: the sites found by hand were fixed, and twelve were
 * missed -- including the Review queue's own apply/reject, and one file where a
 * comment explaining that `invokeSafe` swallows the rejection sat directly above
 * an `invokeSafe` call. Hand-auditing does not close a class. This does.
 */

const rules = {
  "no-invokesafe-on-void-command": {
    meta: {
      type: "problem",
      docs: {
        description:
          "Forbid invokeSafe() on a Tauri command that returns nothing, because its success value and invokeSafe's failure value are both null",
      },
      schema: [
        {
          type: "object",
          properties: { tauriSrc: { type: "string" } },
          additionalProperties: false,
        },
      ],
      messages: {
        voidViaInvokeSafe:
          '"{{cmd}}" returns Result<(), _>, so it resolves to null on SUCCESS -- and invokeSafe returns null on FAILURE. The two are indistinguishable, and any catch block around this call is unreachable. Use the raw `invoke` from @tauri-apps/api/core and surface the rejection to the user.',
      },
    },
    create(context) {
      const tauriSrc = context.options?.[0]?.tauriSrc ?? DEFAULT_TAURI_SRC;
      let voidCommands;
      return {
        CallExpression(node) {
          const callee = node.callee;
          const isInvokeSafe =
            (callee.type === "Identifier" && callee.name === "invokeSafe") ||
            (callee.type === "MemberExpression" &&
              callee.property.type === "Identifier" &&
              callee.property.name === "invokeSafe");
          if (!isInvokeSafe) return;

          const first = node.arguments[0];
          // A non-literal command name cannot be checked statically. Rather than
          // guess, say nothing -- a false positive here would get the rule
          // disabled, which costs more than the miss.
          if (!first || first.type !== "Literal" || typeof first.value !== "string") return;

          voidCommands ??= collectVoidCommands(tauriSrc);
          if (!voidCommands.has(first.value)) return;

          context.report({
            node: first,
            messageId: "voidViaInvokeSafe",
            data: { cmd: first.value },
          });
        },
      };
    },
  },
};

export default { rules };
