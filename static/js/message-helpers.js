function convertToLocalTime(isoTimestamp) {
    const date = new Date(isoTimestamp);
    const now = new Date();

    const isSameDay = date.getDate() === now.getDate() &&
        date.getMonth() === now.getMonth() &&
        date.getFullYear() === now.getFullYear();

    const isYesterday = date.getDate() === now.getDate() - 1 &&
        date.getMonth() === now.getMonth() &&
        date.getFullYear() === now.getFullYear();

    if (isSameDay) {
        const timeOptions = {hour: '2-digit', minute: '2-digit'};
        return date.toLocaleTimeString('en-US', timeOptions);
    }

    if (isYesterday) {
        const timeOptions = {hour: '2-digit', minute: '2-digit'};
        return `Yesterday at ${date.toLocaleTimeString('en-US', timeOptions)}`;
    }

    if (date.getFullYear() === now.getFullYear()) {
        const dateOptions = {month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'};
        return date.toLocaleDateString('en-US', dateOptions);
    }

    const dateOptions = {year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'};
    return date.toLocaleDateString('en-US', dateOptions);
}