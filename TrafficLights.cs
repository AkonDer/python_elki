using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using Org.BouncyCastle.Asn1.Cms;

namespace Elki
{
    internal class TrafficLights : ElkiTimer
    {
        private List<string> _closeBar = new List<string>();
        private List<string> _openBar = new List<string>();

        private double _time;
        private double _timeNow;

        Image _imageCloseBar;
        Image _imageOpenBar;

        private DateTime _nearOpenTime;
        private DateTime _nearCloseTime;



        public TrafficLights(double dt, string openBar, string closeBar) : base(dt)
        {
            _openBar = File.ReadAllLines(openBar).ToList();
            _closeBar = File.ReadAllLines(closeBar).ToList();

            _imageCloseBar = Image.FromFile(@"resources\close.png");
            _imageOpenBar = Image.FromFile(@"resources\open.png");
        }

        protected override void OnTimer(object source, ElapsedEventArgs e)
        {
            _timeNow = ConvertTimeToDouble(DateTime.Now);

            _nearOpenTime = findNearTime(_openBar);
            _nearCloseTime = findNearTime(_closeBar);
            
            double deltaCloseBar = ConvertTimeToDouble(_nearCloseTime) - _timeNow;
            double deltaOpenBar = ConvertTimeToDouble(_nearOpenTime) - _timeNow;

            Bitmap b = new Bitmap(170, 100);
            using (Graphics g = Graphics.FromImage(b))
            {
                // Create fonts and brush.
                SolidBrush drawBrush = new SolidBrush(Color.DarkBlue);
                Font drawFont1 = new Font("Arial", 20, FontStyle.Bold);
                Font drawFont2 = new Font("Arial", 24, FontStyle.Bold);

                // Set format of string.
                StringFormat drawFormat = new StringFormat();

                // Рисуем линии
                Pen ePen = new Pen(Color.DarkBlue, 1);

                g.Clear(Color.White);

                int whImage = 51;
                int xImage = 5;
                int yImage = 50 - whImage/2 + 14;
                int xTextTime = 63;
                int yTextTime = 50;
                

                if (deltaCloseBar == 0)
                {
                    g.DrawImage(_imageCloseBar, xImage, yImage, whImage, whImage);
                    g.DrawString(_nearOpenTime.Subtract(DateTime.Now).ToString(@"h\:mm\:ss"), drawFont1, drawBrush, xTextTime, yTextTime, drawFormat);
                }
                else if (deltaOpenBar == 0)
                {
                    g.DrawImage(_imageOpenBar, xImage, yImage, whImage, whImage);
                    g.DrawString(_nearCloseTime.Subtract(DateTime.Now).ToString(@"h\:mm\:ss"), drawFont1, drawBrush, xTextTime, yTextTime, drawFormat);
                }
                else if (deltaCloseBar != 0 && deltaOpenBar != 0 && deltaCloseBar < deltaOpenBar)
                {
                    g.DrawImage(_imageOpenBar, xImage, yImage, whImage, whImage);
                    g.DrawString(_nearCloseTime.Subtract(DateTime.Now).ToString(@"h\:mm\:ss"), drawFont1, drawBrush, xTextTime, yTextTime, drawFormat);
                }
                else if (deltaCloseBar != 0 && deltaOpenBar != 0 && deltaCloseBar > deltaOpenBar)
                {
                    g.DrawImage(_imageCloseBar, xImage, yImage, whImage, whImage);
                    g.DrawString(_nearOpenTime.Subtract(DateTime.Now).ToString(@"h\:mm\:ss"), drawFont1, drawBrush, xTextTime, yTextTime, drawFormat);
                }

                g.DrawString("ПЕРЕЕЗД", drawFont2, drawBrush, 5, 0, drawFormat);

                //// рисуем линии
                //g.DrawLine(ePen, 78, 34, 160, 34);
                //g.DrawLine(ePen, 78, 68, 160, 68);

                ////Рисуем вычесленные времена отправления электричек
                //g.DrawString(time1, drawFont1, drawBrush, 87, 7, drawFormat);
                //g.DrawString(time3, drawFont1, drawBrush, 87, 70, drawFormat);

                //g.DrawString(time2, drawFont2, drawBrush, 72, 33, drawFormat);

                b.Save(@"output\trafficlights.bmp", ImageFormat.Bmp);
                b.Save(@"output\trafficlights2.bmp", ImageFormat.Bmp);
            }

        }

        private DateTime findNearTime(List<string> listTimes)
        {
            foreach (var item in listTimes)
            {
                _time = ConvertTimeToDouble(Convert.ToDateTime(item));
                if (_time - _timeNow >= 0) return Convert.ToDateTime(item);
            }
            return Convert.ToDateTime(listTimes[0]);
        }

        private double ConvertTimeToDouble(DateTime dt)
        {
            return dt.Hour + Convert.ToDouble(dt.Minute) / 60;
        }
    }
}
