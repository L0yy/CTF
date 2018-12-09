#include <iostream>
#include <tchar.h>
#include <Windows.h>
#include "InputBuffer.h"
using std::cout;
using std::endl;

int _tmain(int argc, _TCHAR* argv[])
{    
    /************************************函数说明*********************************************
    * 函数名：CreateFile                                                                     *
    * 类型：Win32 API函数                                                                    *
    * 作用：这是一多功能的函数，可打开或创建如：控制台，通信资源，目录（只读打开），                    *
    * 磁盘驱动器，文件，邮槽，管道等对象，并返回可访问的句柄：。                                     *
    * 参数说明：                                                                             *
    * LPCTSTR lpFileName ： 普通文件名或者设备文件名                                            *
    * DWORD dwDesiredAccess ： 访问对象的权限，希望以哪种方式打开,建议两者兼备。                    *
    * DWORD dwShareMode ： 共享模式，建议两者兼备。                                             *
    * LPSECURITY_ATTRIBUTES ： 用来设定一个指向是否由子进程返回的句柄可以被继承                     *
    * DWORD dwCreationDisposition ： 表示判断文件存在或不存在，按需求如何创建                      *
    * DWORD dwFlagsAndAttributes ： 文件标志或设备属性                                         *
    * HANDLE hTemplateFile ：模板文件,给创建的文件提供文件属性和扩展属性，一般为空                   *
    * 返回值： 获取设备的句柄                                                                   *
    *****************************************************************************************/
    HANDLE  DeviceHandle = CreateFile(
        L"\\\\.\\AppSymbolLink",              //\\??\\设备符号链接名称,注意这里要用 L 宽字符转换
        GENERIC_READ | GENERIC_WRITE,    
        FILE_SHARE_READ | FILE_SHARE_WRITE,   
        NULL,                             
        OPEN_EXISTING,                        //枚举：OPEN_EXISTING 表示文件必须已经存在。
        FILE_ATTRIBUTE_NORMAL,                 //此枚举表示文件没有其他属性集。
        NULL);                                 //模板文件,一般为空
    if (DeviceHandle == INVALID_HANDLE_VALUE){
        printf("获取文件或设备句柄失败！！");
        getchar();                            //读取清除缓冲区字符
        return -1;
    }

        printf("获取驱动程序句柄成功 \n");
        int a=10, b=20, c=30,e=0,f=0,g=0;
        InputBuffer(DeviceHandle, a, b, c);
        for (int i = 0; i < 3; i++)
        {
            switch (i){
            case 0:{
                       e = OtnC[i];
            }
            case 1:{
                       f = OtnC[i];
            }
            case 2:{
                       g = OtnC[i];
            }
            } //End switch (i)
        }  //End for 

    printf("a=%d,b=%d,c=%d\n",e, f, g);    
    CloseHandle(DeviceHandle);            //过程完成后，最好关闭句柄    
    cout << "驱动通讯完成" << endl;
    system("pause");
}