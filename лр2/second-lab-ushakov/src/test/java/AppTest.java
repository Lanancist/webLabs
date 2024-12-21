import org.joda.time.LocalDateTime;
import org.junit.Test;
import org.mockito.Mockito;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.when;

/**
 * Unit test for simple App.
 */
public class AppTest {

    @Test
    public void currentTimeTest() {
        App mockApp = Mockito.mock(App.class);
        LocalDateTime fixedTime = LocalDateTime.parse("2024-12-21T18:54:00");
        when(mockApp.getCurrentLocalDateTime()).thenReturn(fixedTime);

        LocalDateTime returnedTime = someFunctionUsingApp(mockApp);
        assertEquals(fixedTime, returnedTime);
    }

    private LocalDateTime someFunctionUsingApp(App app) {
        return app.getCurrentLocalDateTime();
    }
}
