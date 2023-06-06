# Langchain Notes

## Capabilities
- Langchain agents take in a set of tools
- Describe the environment (What tools are available)
- Agents use tools (embodied)
- Prompt agent to complete task
- Agent will use knowledge of tools it has available, execute task (invoke service, search index, math evaluation / arithmetic, etc.)
- Agents can prompt other agents
- Actions the agent will make will execute tools
- Service works by receiving a context from the game server or client

## Flow
### High Level Flow
`Game Server (Multiplayer) / Client (Single Player) -> Context (NPC Observation) -> SimulacrAI Service (Multiprotocol) -> Langchain Prompt -> Langchain Agent (Loop) -> Action -> Tools -> Update Context -> LLM -> Natural Language Output -> Natural Language Parser -> Structured Data -> Service Response`
### Tool Example
`Agent Prompt -> Vector Database -> Context Update`

### Long Term Memory to Short Term Memory
`Vector Database -> LLM Context -> LLM Prompt`

## Definition
### Observation
- Example: NPC sees player walk into their shop, sees another NPC at a bar, sees another NPC walk by in town
### Agent
- Langchain definition: "An Agent is a wrapper around a model, which takes in user input and returns a response corresponding to an “action” to take and a corresponding “action input”."
- Creates context for LLM
- Agents can talk to other agents or players  
- Starts with a purpose, could be hand written, could be deterministic, when the purpose is done, blocked, or doesn't know what to do, falls back on AI
- Example: Goal is to get to town, initially says it can go straight, but finds out that there are walls in it's path, calls a AI pathfinding tool
- Example: Go to new town, but to go to new town you have to leave the town first, starts looking at map, finds out the map is not complete and doesn't contain location for new town, needs to find a new map, asks a player, goes to a merchant to buy a map, etc.

## Considerations
### Make sure to:
- Understand difference between short term and long term memory

### Potential Issues:
- Most open source models have about 4k context limit
- Takes up to 1k to initialize tools
- Be careful with context limit

### Tools Needed
- Arithmetic (Shopkeeper bartering, Read stats of items such as weapons, armor, sword, magic spells, etc.)
- Pathfinding
- Vector / Graph / Relational database
- Dictionary