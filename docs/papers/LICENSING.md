# Determinex Licensing

Determinex is **free and open source software**, licensed under the
**GNU Affero General Public License, version 3 (AGPLv3)** — an OSI-approved
copyleft license.

## Plain-English Summary

Permitted, no separate agreement needed:

- use Determinex for anything — personal, research, commercial, hosted;
- modify it;
- redistribute it, modified or not; and
- charge money for services built on it.

The one real condition: **if you distribute Determinex, or run a modified
version as a network service that others interact with, you must make the
corresponding source code available to those users under AGPLv3.** That's
the "Affero" clause — it closes the loophole plain GPL has for SaaS: you
can't take Determinex, improve it privately, and offer it as a hosted
service without releasing your changes back.

The controlling legal terms are in [../LICENSE](../LICENSE). This file is
only an explanatory guide and does not replace the license.

## Why AGPLv3 and Not MIT / Apache

MIT and Apache-style licenses are permissive: anyone can take the code,
modify it, and ship a closed, proprietary derivative with no obligation to
share anything back. That's a legitimate choice for some projects — it
isn't the right one for a correctness engine whose entire value is the
verification loop itself.

AGPLv3 keeps that loop open permanently:

- source visibility remains public, forever, for every derivative;
- commercial use is unrestricted — no separate license, no fee;
- network/hosted use of a modified version still requires releasing source
  to the users of that service (the "Affero" clause, absent from plain
  GPLv3);
- the project **is** OSI open source, full stop.

## Models, Datasets, and Third-Party Components

Determinex code and any fine-tuned model artifacts released alongside it
are covered by AGPLv3 unless a model card or file-specific notice states
otherwise.

Third-party dependencies, base models, datasets, benchmarks, and upstream
task repositories remain governed by their own licenses and terms. The
Determinex license does not grant rights the project does not itself own.

## Contact

For questions about licensing, contributions, or anything not covered
above, open a [GitHub Discussion](https://github.com/DarthCeltic/determinex/discussions).
