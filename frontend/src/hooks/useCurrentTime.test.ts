import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';


describe('useCurrentTime Hook', () => {
    beforeAll(() => {
        jest.useFakeTimers();
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    it('should display time correctly', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toMatch(/^\d{2}:\d{2}:\d{2}$/);
    });

    it('should return current time', () => {
        jest.setSystemTime(new Date('2024-01-01 09:00:00').getTime());
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toBe('09:00:00');
    });

    it('should update time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).not.toBe(initialTime);
    });
});