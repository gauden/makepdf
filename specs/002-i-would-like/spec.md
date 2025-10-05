# Feature Specification: Use Current Working Directory

**Feature Branch**: `002-i-would-like`  
**Created**: 2025-10-05  
**Status**: Draft  
**Input**: User description: "I would like to tweak a feature. The app will often be run from directories that outside the project tree. The app should use the current working directory where the user is operating, not the directory where the app or its launcher are located."

## Execution Flow (main)
```
1. Parse user description from Input
   → If empty: ERROR "No feature description provided"
2. Extract key concepts from description
   → Identify: actors, actions, data, constraints
3. For each unclear aspect:
   → Mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
   → If no clear user flow: ERROR "Cannot determine user scenarios"
5. Generate Functional Requirements
   → Each requirement must be testable
   → Mark ambiguous requirements
6. Identify Key Entities (if data involved)
7. Run Review Checklist
   → If any [NEEDS CLARIFICATION]: WARN "Spec has uncertainties"
   → If implementation details found: ERROR "Remove tech details"
8. Return: SUCCESS (spec ready for planning)
```

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
2. **Don't guess**: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
3. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
4. **Common underspecified areas**:
   - User types and permissions
   - Data retention/deletion policies  
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a user, I want to run `makepdf` from any directory on my system, so that it processes the files in that directory, not the directory where the application is installed.

## Clarifications
### Session 2025-10-05
- Q: When no processable files are found in the target directory, how should the system report this to the user? → A: A more verbose message to stderr, explaining what file types are supported.
- Q: How should the tool handle a corrupted or unreadable input file when other valid files are also present in the input? → A: Stop processing immediately and report an error for the problematic file.
- Q: Is there a maximum number of files or a total input size the tool should aim to support in a single run? → A: No specific limit; the tool should handle as many files as the system memory allows.

---

### Acceptance Scenarios
1. **Given** a user is in a directory `/path/to/my/images` containing image files, **When** they run the command `makepdf .`, **Then** the system should create a PDF file from the images located in `/path/to/my/images`.
2. **Given** a user is in a directory `/path/to/empty/dir` with no processable files, **When** they run the command `makepdf .`, **Then** the system should output a verbose message to stderr explaining the supported file types and that no such files were found.

### Edge Cases
- How does the system behave if the user provides an absolute path to a directory as an argument? The system should prioritize the specified path over the current working directory.
- How does the system handle a situation where it does not have read permissions for the current working directory? It should gracefully exit and inform the user of the permission error.
- What happens if a corrupted or unreadable file is provided as input? The system must stop processing and report a file-specific error.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST default to using the user's current working directory to search for files when no explicit paths are provided as arguments.
- **FR-002**: The system MUST NOT use the application's installation directory or the launcher script's location as a basis for finding files.
- **FR-003**: The system MUST correctly handle and prioritize absolute or relative file/directory paths when they are provided as command-line arguments, overriding the default behavior.
- **FR-004**: The system MUST detect and report an appropriate error message if the current working directory is not readable due to permissions issues.
- **FR-005**: System MUST output a verbose error message to stderr when no processable files are found, indicating which file types are supported.
- **FR-006**: The system MUST halt processing and report a specific error if any input file is found to be corrupted or unreadable.

### Non-Functional Requirements
- **NFR-001**: The system should be able to process a number of files limited only by the available system memory.

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

### Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] Requirements are testable and unambiguous  
- [ ] Success criteria are measurable
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

---

## Execution Status
*Updated by main() during processing*

- [ ] User description parsed
- [ ] Key concepts extracted
- [ ] Ambiguities marked
- [ ] User scenarios defined
- [ ] Requirements generated
- [ ] Entities identified
- [ ] Review checklist passed

---