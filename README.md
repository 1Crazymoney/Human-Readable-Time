# Human-Readable-Time
The module includes a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59). Code snippet for converting amount of time given by number of seconds into some human readable form. The function should receive a number and output a string like this: hh:mm:ss.
