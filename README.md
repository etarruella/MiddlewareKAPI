# MiddlewareKAPI

A lightweight middleware service that connects to a Java-based WebSocket server to process, filter, and route real-time event-driven messages.

## Overview

MiddlewareKAPI acts as a bridge between WebSocket clients and the game server, handling subscriptions and dispatching event notifications about player and server state changes.

## Message Formats

Messages use JSON format and are categorized by `type` fields to distinguish player-related and server-related events.


### Player Event Messages

Used for subscribing, unsubscribing, and receiving player-related events.

#### Subscription Example

```json
{
  "type": "PlayerEvent",
  "action": "subscribe",
  "event": "PlayerHealthChangeEvent",
  "playerID": "4f7d0c4e-3fd7-4ad7-9f7d-c97b7f089b25"
}
```

### Server Event Messages

Used by the server to broadcast lifecycle and operational events.

#### Server Event Example

```json
{
  "type": "ServerEvent",
  "action": "subscribe",
  "event": "ServerStartEvent"
}
```

## Usage

* Clients send **subscription** messages to listen for specific player events.
* The server emits **event** messages when changes occur.
* MiddlewareKAPI filters, processes, and forwards these messages as needed.

## Supported Player Events

Some of the player events you can subscribe to include:

* `PlayerHealthChangeEvent`
* `PlayerPositionChangeEvent`
* `PlayerDeathEvent`
* `PlayerJoinEvent`
* *and more (see PlayerEventType enum)*

## Supported Server Events

Server events include:

* `ServerStartEvent`
* `ServerStopEvent`
* `ServerReloadEvent`
* `ServerPlayerCountChangeEvent`
* *and more (see ServerEventType enum)*
